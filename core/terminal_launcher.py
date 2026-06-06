import os
import platform
import sys


def running_in_terminal():
    return sys.stdin.isatty() and sys.stdout.isatty()


def terminal_profile_summary():
    system = platform.system() or "Desconhecido"
    if system == "Darwin":
        system = "macOS"

    return {
        "system": system,
        "terminal": os.environ.get("TERM_PROGRAM") or os.environ.get("TERM") or "terminal padrao",
        "font": "Fira Code incluido no pacote; aplicacao depende do terminal/instalador para ativar ligaduras.",
    }
