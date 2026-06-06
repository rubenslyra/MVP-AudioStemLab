import argparse
import os
import platform
import shutil
from pathlib import Path


def copy_if_exists(source, target):
    source_path = Path(source)
    if source_path.exists():
        if source_path.is_dir():
            shutil.copytree(source_path, target, dirs_exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, target)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--platform", default=platform.system().lower())
    args = parser.parse_args()

    root = Path.cwd()
    dist_app = root / "dist" / "AudioStemLab"
    if not dist_app.exists():
        raise SystemExit("dist/AudioStemLab not found. Run PyInstaller first.")

    package_name = f"AudioStemLab-{args.version}-{args.platform}"
    package_dir = root / "release_dist" / package_name
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True)

    shutil.copytree(dist_app, package_dir / "AudioStemLab")
    copy_if_exists(root / "README.md", package_dir / "README.md")
    copy_if_exists(root / "CHANGELOG.md", package_dir / "CHANGELOG.md")
    copy_if_exists(root / "VERSION", package_dir / "VERSION")
    copy_if_exists(root / "LICENSE", package_dir / "LICENSE")
    copy_if_exists(root / "docs" / "releases" / f"{args.version}.md", package_dir / "RELEASE_NOTES.md")
    copy_if_exists(root / "launchers", package_dir / "launchers")

    install_note = package_dir / "HOW_TO_RUN.txt"
    install_note.write_text(
        "\n".join(
            [
                "RLLABS Audio Stem Lab",
                f"Version: {args.version}",
                "",
                "This portable package includes the application runtime.",
                "End users do not need to install Python or activate a virtual environment.",
                "",
                "How to run:",
                "- Linux: open launchers/audiostemlab-linux.sh or run AudioStemLab/AudioStemLab.",
                "- Windows: open launchers/audiostemlab-windows.bat or run AudioStemLab/AudioStemLab.exe.",
                "- macOS: open launchers/audiostemlab-macos.command or run AudioStemLab/AudioStemLab.",
                "",
                "Use only audio files you own or are authorized to process.",
            ]
        ),
        encoding="utf-8",
    )

    archive_base = root / "release_dist" / package_name
    shutil.make_archive(str(archive_base), "zip", package_dir)
    print(f"Created {archive_base}.zip")


if __name__ == "__main__":
    main()
