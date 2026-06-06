import importlib.util
import os
import re
import subprocess
import sys
import time
from pathlib import Path

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

    def build_command(self, audio_path, mode, output_format, output_dir=None):
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
            str(output_dir or self.output_dir),
        ]

        if mode_config["two_stems"]:
            command.extend(["--two-stems", mode_config["two_stems"]])

        if output_format == "mp3":
            command.extend(["--mp3", "--mp3-bitrate", "320"])
        elif output_format == "flac":
            command.append("--flac")

        command.append(audio_path)
        return command

    def _run_with_progress(self, command, env, progress_callback=None):
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            env=env,
        )
        buffer = ""
        started_at = time.monotonic()

        while True:
            char = process.stdout.read(1) if process.stdout else ""
            if char == "" and process.poll() is not None:
                break

            if not char:
                continue

            if char in ("\r", "\n"):
                line = buffer.strip()
                buffer = ""
                if line and progress_callback:
                    progress_callback(self._progress_message(line, started_at))
            else:
                buffer += char

        if buffer.strip() and progress_callback:
            progress_callback(self._progress_message(buffer.strip(), started_at))

        return_code = process.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, command)

    def _progress_message(self, line, started_at):
        percent_match = re.search(r"(\d{1,3})%", line)
        percent = None
        if percent_match:
            percent = min(100, int(percent_match.group(1)))

        elapsed = int(time.monotonic() - started_at)
        minutes, seconds = divmod(elapsed, 60)
        elapsed_text = f"{minutes} min {seconds:02d} s" if minutes else f"{seconds} s"

        if percent is not None:
            return f"Processando audio: {percent}% concluido | tempo decorrido: {elapsed_text}"

        if "Separating track" in line:
            return "Analisando e separando a musica..."

        if "Separated tracks will be stored" in line:
            return "Preparando pasta de destino dos stems..."

        return None

    def separate(self, audio_path, mode, output_format="wav", output_dir=None, progress_callback=None):
        if importlib.util.find_spec("demucs") is None:
            raise MissingDependencyError("Demucs nao encontrado no ambiente do aplicativo.")

        self.paths.ensure()
        selected_output_dir = Path(output_dir) if output_dir else self.output_dir
        selected_output_dir.mkdir(parents=True, exist_ok=True)
        command = self.build_command(audio_path, mode, output_format, selected_output_dir)

        env = os.environ.copy()
        temp_dir = str(self.paths.temp_dir)
        env["TMPDIR"] = temp_dir
        env["TEMP"] = temp_dir
        env["TMP"] = temp_dir
        env["TORCHINDUCTOR_CACHE_DIR"] = str(self.paths.cache_dir / "torch_inductor")
        env["PYTHONWARNINGS"] = "ignore:The.*parameter is .*supported by TorchCodec AudioEncoder:UserWarning"

        self._run_with_progress(command, env, progress_callback)
