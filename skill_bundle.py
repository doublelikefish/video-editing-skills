#!/usr/bin/env python3
"""Build or install the portable production Skills; Python standard library only."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import tempfile
import zipfile


SKILLS = (
    "video-editing", "media-screening", "video-preproduction", "video-first-cut",
    "video-color", "video-motion", "video-sound", "video-subtitles",
    "video-review", "video-delivery",
)
BASIC_SKILLS = ("video-production",)
COMPLETE_SKILLS = BASIC_SKILLS + tuple(name for name in SKILLS if name != "video-editing")
PROFILES = {"basic": BASIC_SKILLS, "complete": COMPLETE_SKILLS, "pro": SKILLS}
ALL_SKILLS = BASIC_SKILLS + SKILLS


def skill_files(root: Path, name: str) -> dict[str, bytes]:
    """Reject links and unsupported payloads instead of copying machine bindings."""
    folder = root / name
    if folder.is_symlink() or not folder.is_dir():
        raise ValueError(f"Missing regular Skill directory: {folder}")
    result = {}
    for path in sorted(folder.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Skill bundle cannot contain symlinks: {path}")
        if path.is_dir():
            continue
        rel = path.relative_to(folder).as_posix()
        allowed = rel == "SKILL.md" or rel == "agents/openai.yaml" or (
            rel.startswith("references/") and path.suffix == ".md"
        )
        if not path.is_file() or not allowed:
            raise ValueError(f"Unexpected bundle file; review packaging scope: {path}")
        result[rel] = path.read_bytes()
    if "SKILL.md" not in result:
        raise ValueError(f"Missing SKILL.md: {folder}")
    return result


def same_tree(target: Path, files: dict[str, bytes]) -> bool:
    if target.is_symlink() or not target.is_dir():
        return False
    actual = {}
    for path in target.rglob("*"):
        if path.is_symlink():
            return False
        if path.is_file():
            actual[path.relative_to(target).as_posix()] = path.read_bytes()
        elif not path.is_dir():
            return False
    return actual == files


def build(source: Path, out: Path, profile: str = "pro") -> dict:
    if profile not in PROFILES:
        raise ValueError("Select a known bundle profile: basic, complete or pro")
    source = source.resolve()
    payload = {}
    names = PROFILES[profile]
    for name in names:
        for relative, data in skill_files(source, name).items():
            payload[f"video-skills/skills/{name}/{relative}"] = data
    payload["video-skills/skill_bundle.py"] = Path(__file__).read_bytes()
    guide_name = {"basic": "video-skills-basic.md",
                  "complete": "video-skills-complete.md",
                  "pro": "video-skills.md"}[profile]
    guide = (source.parent / "packaging" / guide_name).read_bytes()
    payload["video-skills/README.md"] = (
        f"本包：{profile}；包含 {', '.join(names)}。\n\n".encode() + guide
    )
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    content = buffer.getvalue()
    out = out.expanduser().absolute()
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("xb") as stream:
        stream.write(content)
    return {"archive": str(out), "profile": profile, "skills": list(names), "files": len(payload),
            "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()}


def install(source: Path, dest: Path, names: list[str], replace: bool) -> dict:
    source = source.expanduser().resolve()
    dest = dest.expanduser().resolve()
    names = list(dict.fromkeys(names))
    if not names or any(name not in ALL_SKILLS for name in names):
        raise ValueError("Select known Skill names")
    # A destination within source would invalidate the source on replacement.
    if source == dest or source in dest.parents or dest in source.parents:
        raise ValueError("Source and destination must be separate directories")
    payloads = {name: skill_files(source, name) for name in names}
    unchanged = [name for name in names if same_tree(dest / name, payloads[name])]
    changes = [name for name in names if name not in unchanged]
    conflicts = [name for name in changes if os.path.lexists(dest / name)]
    if conflicts and not replace:
        raise ValueError("Existing Skills differ; no changes made. Use --replace to "
                         "back up and replace: " + ", ".join(conflicts))
    if not changes:
        return {"destination": str(dest), "installed": [], "unchanged": unchanged,
                "backup": None}
    dest.mkdir(parents=True, exist_ok=True)
    # Keep backup outside the discoverable Skill root. Same filesystem for rename.
    backup = Path(tempfile.mkdtemp(prefix="video-skills-backup-", dir=dest.parent)) if conflicts else None
    staged = Path(tempfile.mkdtemp(prefix=".video-skills-stage-", dir=dest))
    installed, backed_up = [], []
    try:
        for name in changes:
            for relative, data in payloads[name].items():
                path = staged / name / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
        for name in changes:
            target = dest / name
            if name in conflicts:
                target.rename(backup / name)
                backed_up.append(name)
            (staged / name).rename(target)
            installed.append(name)
    except Exception:
        for name in reversed(installed):
            shutil.rmtree(dest / name)
        for name in reversed(backed_up):
            (backup / name).rename(dest / name)
        if backup is not None and not any(backup.iterdir()):
            backup.rmdir()
        raise
    finally:
        shutil.rmtree(staged)
    return {"destination": str(dest), "installed": installed, "unchanged": unchanged,
            "backup": str(backup) if backup else None}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    builder = commands.add_parser("build", help="Build a ZIP from the source checkout")
    builder.add_argument("--source", type=Path,
                         default=Path(__file__).resolve().parent.parent / "skills")
    builder.add_argument("--out", type=Path, required=True)
    builder.add_argument("--profile", choices=tuple(PROFILES), default="pro",
                         help="complete: current coordinator and nine stage Skills; "
                              "basic: single-file guide; pro: legacy ten-Skill bundle (default)")
    installer = commands.add_parser("install", help="Install all or selected Skills")
    installer.add_argument("--source", type=Path,
                           default=Path(__file__).resolve().parent / "skills")
    codex_skills = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills"
    installer.add_argument("--dest", type=Path, default=codex_skills)
    installer.add_argument("--skill", action="append", choices=ALL_SKILLS,
                           help="Repeat to select Skills; defaults to those included in this package")
    installer.add_argument("--replace", action="store_true",
                           help="Back up existing differing Skills before replacing")
    args = parser.parse_args()
    try:
        if args.command == "build":
            result = build(args.source, args.out, args.profile)
        else:
            source = args.source.expanduser()
            names = args.skill or [name for name in ALL_SKILLS
                                   if os.path.lexists(source / name)]
            result = install(source, args.dest, names, args.replace)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"{exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
