import subprocess
import shutil
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

    def download_audio(self, url):
        if shutil.which("yt-dlp") is None:
            raise MissingDependencyError("yt-dlp nao encontrado no ambiente do aplicativo.")

        command = [
            "yt-dlp",
            "-x",
            "--audio-format",
            "mp3",
            "-o",
            str(self.input_dir / "%(title)s.%(ext)s"),
            url,
        ]

        subprocess.run(command, check=True)
