from core.paths import AppPaths
from core.file_manager import FileManager
from core.separator import AudioSeparator
from core.terminal_ui import TerminalUI


def test_file_manager_ensures_directories(tmp_path):
    paths = AppPaths(
        data_dir=tmp_path / "data",
        cache_dir=tmp_path / "cache",
        input_dir=tmp_path / "data" / "input_audio",
        output_dir=tmp_path / "data" / "output_stems",
        models_dir=tmp_path / "cache" / "models",
        logs_dir=tmp_path / "data" / "logs",
        temp_dir=tmp_path / "cache" / "tmp",
    )

    fm = FileManager(paths)
    fm.ensure_directories()

    assert paths.input_dir.is_dir()
    assert paths.output_dir.is_dir()
    assert paths.models_dir.is_dir()
    assert paths.logs_dir.is_dir()
    assert paths.temp_dir.is_dir()


def test_terminal_ui_methods_run():
    ui = TerminalUI()
    # Apenas garantir que métodos básicos não levantam exceção
    ui.info("teste")
    ui.success("teste")
    ui.error("teste")


def test_separator_builds_mp3_vocal_command(tmp_path):
    paths = AppPaths(
        data_dir=tmp_path / "data",
        cache_dir=tmp_path / "cache",
        input_dir=tmp_path / "data" / "input_audio",
        output_dir=tmp_path / "data" / "output_stems",
        models_dir=tmp_path / "cache" / "models",
        logs_dir=tmp_path / "data" / "logs",
        temp_dir=tmp_path / "cache" / "tmp",
    )
    separator = AudioSeparator(paths)

    command = separator.build_command("song.mp3", "vocals", "mp3")

    assert "-n" in command
    assert "htdemucs" in command
    assert "--two-stems" in command
    assert "vocals" in command
    assert "--mp3" in command
    assert "--mp3-bitrate" in command
    assert "320" in command


def test_separator_builds_extended6_flac_command(tmp_path):
    paths = AppPaths(
        data_dir=tmp_path / "data",
        cache_dir=tmp_path / "cache",
        input_dir=tmp_path / "data" / "input_audio",
        output_dir=tmp_path / "data" / "output_stems",
        models_dir=tmp_path / "cache" / "models",
        logs_dir=tmp_path / "data" / "logs",
        temp_dir=tmp_path / "cache" / "tmp",
    )
    separator = AudioSeparator(paths)

    command = separator.build_command("song.mp3", "extended6", "flac")

    assert "htdemucs_6s" in command
    assert "--flac" in command
    assert "--two-stems" not in command
