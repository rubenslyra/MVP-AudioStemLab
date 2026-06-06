from pathlib import Path


class FileDialogUnavailable(RuntimeError):
    pass


def _tk_root():
    try:
        import tkinter as tk
    except ImportError as error:
        raise FileDialogUnavailable("Seletor de arquivos indisponivel neste sistema.") from error

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    return root


def choose_audio_file(initial_dir):
    root = _tk_root()
    from tkinter import filedialog

    try:
        selected = filedialog.askopenfilename(
            parent=root,
            title="Escolha o arquivo de audio",
            initialdir=str(initial_dir),
            filetypes=[
                ("Audio", "*.mp3 *.wav *.flac *.m4a *.aac *.ogg *.webm"),
                ("MP3", "*.mp3"),
                ("WAV", "*.wav"),
                ("FLAC", "*.flac"),
                ("Todos os arquivos", "*.*"),
            ],
        )
    finally:
        root.destroy()

    return Path(selected) if selected else None


def choose_output_folder(initial_dir):
    root = _tk_root()
    from tkinter import filedialog

    try:
        selected = filedialog.askdirectory(
            parent=root,
            title="Escolha a pasta de destino dos stems",
            initialdir=str(initial_dir),
            mustexist=False,
        )
    finally:
        root.destroy()

    return Path(selected) if selected else None
