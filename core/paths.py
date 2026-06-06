import os
import sys
from dataclasses import dataclass
from pathlib import Path


APP_NAME = "AudioStemLab"


def _user_data_root() -> Path:
    if sys.platform == "win32":
        base = os.environ.get("APPDATA")
        if base:
            return Path(base) / APP_NAME
        return Path.home() / "AppData" / "Roaming" / APP_NAME

    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / APP_NAME

    base = os.environ.get("XDG_DATA_HOME")
    if base:
        return Path(base) / APP_NAME
    return Path.home() / ".local" / "share" / APP_NAME


def _user_cache_root() -> Path:
    if sys.platform == "win32":
        base = os.environ.get("LOCALAPPDATA")
        if base:
            return Path(base) / APP_NAME / "Cache"
        return Path.home() / "AppData" / "Local" / APP_NAME / "Cache"

    if sys.platform == "darwin":
        return Path.home() / "Library" / "Caches" / APP_NAME

    base = os.environ.get("XDG_CACHE_HOME")
    if base:
        return Path(base) / APP_NAME
    return Path.home() / ".cache" / APP_NAME


@dataclass(frozen=True)
class AppPaths:
    data_dir: Path
    cache_dir: Path
    input_dir: Path
    output_dir: Path
    models_dir: Path
    logs_dir: Path
    temp_dir: Path

    @classmethod
    def default(cls) -> "AppPaths":
        if getattr(sys, "frozen", False):
            data_dir = _user_data_root()
            cache_dir = _user_cache_root()
        else:
            data_dir = Path(__file__).resolve().parents[1]
            cache_dir = data_dir / ".cache" / APP_NAME

        return cls(
            data_dir=data_dir,
            cache_dir=cache_dir,
            input_dir=data_dir / "input_audio",
            output_dir=data_dir / "output_stems",
            models_dir=cache_dir / "models",
            logs_dir=data_dir / "logs",
            temp_dir=cache_dir / "tmp",
        )

    def ensure(self) -> None:
        for path in (
            self.data_dir,
            self.cache_dir,
            self.input_dir,
            self.output_dir,
            self.models_dir,
            self.logs_dir,
            self.temp_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)
