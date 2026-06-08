import shutil
import subprocess
import sys
from pathlib import Path

from core.paths import AppPaths


class MissingDependencyError(RuntimeError):
    pass


class FileManager:
    def __init__(self, paths=None):
        self.paths = paths or AppPaths.default()
        self.input_dir = self.paths.input_dir
        self.output_dir = self.paths.output_dir

    def ensure_directories(self):
        self.paths.ensure()

    def file_exists(self, path):
        return Path(path).is_file()

    def build_download_command(self, url, output_dir=None):
        target_dir = Path(output_dir) if output_dir else self.input_dir
        output_template = str(target_dir / "%(title)s.%(ext)s")

        try:
            import yt_dlp  # noqa: F401

            return [
                sys.executable,
                "-m",
                "yt_dlp",
                "-x",
                "--audio-format",
                "mp3",
                "-o",
                output_template,
                url,
            ]
        except ImportError:
            executable = shutil.which("yt-dlp")
            if executable:
                return [
                    executable,
                    "-x",
                    "--audio-format",
                    "mp3",
                    "-o",
                    output_template,
                    url,
                ]

        raise MissingDependencyError(
            "download indisponivel neste pacote: yt-dlp nao foi incluido no ambiente do aplicativo."
        )

    def download_audio(self, url, output_dir=None):
        target_dir = Path(output_dir) if output_dir else self.input_dir
        target_dir.mkdir(parents=True, exist_ok=True)

        command = self.build_download_command(url, target_dir)

        subprocess.run(command, check=True)
