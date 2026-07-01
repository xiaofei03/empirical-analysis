#!/usr/bin/env python3
"""Create or verify a project-local plotting environment for final figures."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import venv
from pathlib import Path


REQUIRED_PACKAGES = ["matplotlib", "pandas", "numpy", "Pillow"]
CN_FONT_CANDIDATES = ["Songti SC", "SimSun", "STSong", "Songti", "Arial Unicode MS"]
EN_FONT_CANDIDATES = ["Times New Roman"]


def run(cmd: list[str], *, cwd: Path | None = None) -> str:
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=True)
    return result.stdout.strip()


def env_python(env_dir: Path) -> Path:
    if sys.platform == "win32":
        return env_dir / "Scripts" / "python.exe"
    return env_dir / "bin" / "python"


def ensure_env(env_dir: Path) -> Path:
    if not env_python(env_dir).exists():
        builder = venv.EnvBuilder(with_pip=True)
        builder.create(env_dir)
    return env_python(env_dir)


def ensure_packages(py: Path, packages: list[str]) -> None:
    missing = []
    probe = (
        "import importlib.util, sys; "
        "missing=[p for p in sys.argv[1:] if importlib.util.find_spec('PIL' if p=='Pillow' else p) is None]; "
        "print('\\n'.join(missing))"
    )
    output = run([str(py), "-c", probe, *packages])
    if output:
        missing = [line.strip() for line in output.splitlines() if line.strip()]
    if missing:
        run([str(py), "-m", "pip", "install", *missing])


def collect_manifest(py: Path) -> dict:
    script = r"""
import importlib.metadata as md
import json
import matplotlib.font_manager as fm
packages = ["matplotlib", "pandas", "numpy", "Pillow"]
fonts = {f.name for f in fm.fontManager.ttflist}
cn = [name for name in %r if name in fonts]
en = [name for name in %r if name in fonts]
print(json.dumps({
  "python": %r,
  "packages": {p: md.version(p) for p in packages},
  "resolved_cn_fonts": cn,
  "resolved_en_fonts": en,
}, ensure_ascii=False, indent=2))
""" % (CN_FONT_CANDIDATES, EN_FONT_CANDIDATES, str(py))
    return json.loads(run([str(py), "-c", script]))


def update_gitignore(project_root: Path, env_name: str) -> None:
    gitignore = project_root / ".gitignore"
    entry = f"{env_name}/"
    existing = gitignore.read_text(encoding="utf-8") if gitignore.exists() else ""
    if entry not in existing.splitlines():
        with gitignore.open("a", encoding="utf-8") as f:
            if existing and not existing.endswith("\n"):
                f.write("\n")
            f.write(f"\n# Local plotting environment for final empirical figures\n{entry}\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--env-name", default=".venv_figures")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--skip-install", action="store_true")
    args = parser.parse_args()

    project_root = args.project_root.expanduser().resolve()
    env_dir = project_root / args.env_name
    py = ensure_env(env_dir)
    if not args.skip_install:
        ensure_packages(py, REQUIRED_PACKAGES)

    manifest = collect_manifest(py)
    manifest["environment"] = str(env_dir)
    manifest["gitignore_entry"] = f"{args.env_name}/"
    manifest["required_packages"] = REQUIRED_PACKAGES

    if not manifest["resolved_cn_fonts"]:
        raise SystemExit("No Chinese academic figure font found. Install Songti/SimSun/STSong or pass a project-specific font.")
    if not manifest["resolved_en_fonts"]:
        raise SystemExit("Times New Roman not found. Install or configure Times New Roman before final English figures.")

    update_gitignore(project_root, args.env_name)

    out = args.manifest or project_root / "figures" / "manifest" / "figure_environment.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
