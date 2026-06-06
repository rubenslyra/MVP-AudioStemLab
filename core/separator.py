import importlib.util
import os
import subprocess
import sys

from core.paths import AppPaths


class MissingDependencyError(RuntimeError):
    pass


MODE_CONFIG = {
    "vocals": {
        "model": "htdemucs",
        "two_stems": "vocals",
    },
    "full4": {
        "model": "htdemucs",
        "two_stems": None,
    },
    "extended6": {
        "model": "htdemucs_6s",
        "two_stems": None,
    },
}

OUTPUT_FORMATS = {"wav", "mp3", "flac"}


class AudioSeparator:
    def __init__(self, paths=None):
        self.paths = paths or AppPaths.default()
        self.output_dir = self.paths.output_dir

    def build_command(self, audio_path, mode, output_format):
        if mode not in MODE_CONFIG:
            raise ValueError(f"Modo de separacao invalido: {mode}")

        if output_format not in OUTPUT_FORMATS:
            raise ValueError(f"Formato de saida invalido: {output_format}")

        mode_config = MODE_CONFIG[mode]
        command = [
            sys.executable,
            "-m",
            "demucs",
            "-n",
            mode_config["model"],
            "-o",
            str(self.output_dir),
        ]

        if mode_config["two_stems"]:
            command.extend(["--two-stems", mode_config["two_stems"]])

        if output_format == "mp3":
            command.extend(["--mp3", "--mp3-bitrate", "320"])
        elif output_format == "flac":
            command.append("--flac")

        command.append(audio_path)
        return command

    def separate(self, audio_path, mode, output_format="wav"):
        if importlib.util.find_spec("demucs") is None:
            raise MissingDependencyError("Demucs nao encontrado no ambiente do aplicativo.")

        self.paths.ensure()
        command = self.build_command(audio_path, mode, output_format)

        env = os.environ.copy()
        temp_dir = str(self.paths.temp_dir)
        env["TMPDIR"] = temp_dir
        env["TEMP"] = temp_dir
        env["TMP"] = temp_dir
        env["TORCHINDUCTOR_CACHE_DIR"] = str(self.paths.cache_dir / "torch_inductor")
        env["PYTHONWARNINGS"] = "ignore:The.*parameter is .*supported by TorchCodec AudioEncoder:UserWarning"

        subprocess.run(command, check=True, env=env)
