from pathlib import Path
import sys

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.version import APP_VERSION


SNAPSHOT_DIR = Path("docs/screenshots")


def save_snapshot(name, render):
    console = Console(record=True, width=110)
    render(console)
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    console.save_svg(str(SNAPSHOT_DIR / f"{name}.svg"), title=f"AudioStemLab {name}")


def header():
    return Panel(
        "[bold]RLLABS AUDIO STEM LAB[/bold]\n"
        f"Local stem separation by AI | v{APP_VERSION} | System: Linux | Desktop: Linux, Windows, macOS\n"
        "Terminal: packaged launcher\n"
        "Use only files you own or are authorized to process.",
        box=box.ROUNDED,
        border_style="cyan",
    )


def snapshot_home(console):
    console.print(header())

    paths = Table(title="Project folders", box=box.SIMPLE, show_lines=False)
    paths.add_column("Type", style="cyan")
    paths.add_column("Path")
    paths.add_row("Input", "/home/user/.local/share/AudioStemLab/input_audio")
    paths.add_row("Default output", "/home/user/.local/share/AudioStemLab/output_stems")
    console.print(paths)

    menu = Table(box=box.SIMPLE_HEAVY, show_header=False, padding=(0, 1))
    menu.add_column("Option", style="cyan", no_wrap=True)
    menu.add_column("Action")
    menu.add_row("1", "Separate local audio")
    menu.add_row("2", "Download authorized audio with yt-dlp")
    menu.add_row("3", "About the project")
    menu.add_row("0", "Exit")
    console.print(menu)
    console.print("[bold]Choose an option[/bold] (1):")


def snapshot_file_selection(console):
    console.print(header())
    console.print("\n[bold]Source file[/bold]")
    console.print("[cyan]1[/cyan] Open system file picker")
    console.print("[cyan]2[/cyan] Type or paste the file path manually")
    console.print("[bold]Choose how to provide the file[/bold] (1): 1")
    console.print("\n[green]OK[/green] Selected file: /Users/tester/Music/song.mp3")

    console.print("\n[bold]Destination folder[/bold]")
    console.print("[cyan]1[/cyan] Use default output_stems folder")
    console.print("[cyan]2[/cyan] Choose another folder")
    console.print("[bold]Choose the destination folder[/bold] (1): 2")
    console.print("[green]OK[/green] Selected folder: /Users/tester/Desktop/AudioStemLab Output")


def snapshot_modes(console):
    console.print(header())
    console.print("\n[bold]Separation mode[/bold]")
    console.print("[cyan]1[/cyan] Vocals + instrumental")
    console.print("[cyan]2[/cyan] Vocals + drums + bass + other")
    console.print("[cyan]3[/cyan] Vocals + drums + bass + guitar + piano/keys + other")
    console.print("[yellow]Note:[/yellow] brass, synthesizers and backing vocals still map to 'other' or 'vocals'.")
    console.print("[bold]Choose the mode[/bold] (1): 3")

    console.print("\n[bold]Output format[/bold]")
    console.print("[cyan]1[/cyan] WAV - highest quality")
    console.print("[cyan]2[/cyan] MP3 - smaller file, 320 kbps")
    console.print("[cyan]3[/cyan] FLAC - high quality with compression")
    console.print("[bold]Choose the format[/bold] (1): 3")


def snapshot_processing(console):
    console.print(header())
    console.print("\n[cyan]INFO[/cyan] Starting separation. On simpler computers this can take some time.")
    console.print("[cyan]INFO[/cyan] Preparing destination folder for stems...")
    console.print("[cyan]INFO[/cyan] Analyzing and separating the song...")
    console.print("[cyan]INFO[/cyan] Processing audio: 25% complete | elapsed time: 1 min 12 s")
    console.print("[cyan]INFO[/cyan] Processing audio: 50% complete | elapsed time: 2 min 28 s")
    console.print("[cyan]INFO[/cyan] Processing audio: 75% complete | elapsed time: 3 min 41 s")
    console.print("[cyan]INFO[/cyan] Processing audio: 100% complete | elapsed time: 4 min 55 s")
    console.print("\n[green]OK[/green] Separation complete. Check: /Users/tester/Desktop/AudioStemLab Output")


def snapshot_release_packages(console):
    console.print(header())
    table = Table(title="Release package guide", box=box.ROUNDED)
    table.add_column("Package")
    table.add_column("Recommended for")
    table.add_column("Notes")
    table.add_row("linux-cpu", "Most Linux testers", "Broad compatibility, no NVIDIA CUDA runtime")
    table.add_row("windows-cpu", "Most Windows testers", "Recommended default package")
    table.add_row("macos-cpu", "macOS testers", "macOS is CPU-only")
    table.add_row("linux-cuda", "Linux with NVIDIA GPU", "Larger package, faster on compatible systems")
    table.add_row("windows-cuda", "Windows with NVIDIA GPU", "Optional performance package")
    console.print(table)


def main():
    snapshots = {
        "01-home": snapshot_home,
        "02-file-and-output-selection": snapshot_file_selection,
        "03-separation-options": snapshot_modes,
        "04-processing-progress": snapshot_processing,
        "05-release-packages": snapshot_release_packages,
    }

    for name, render in snapshots.items():
        save_snapshot(name, render)

    print(f"Generated {len(snapshots)} snapshots in {SNAPSHOT_DIR}")


if __name__ == "__main__":
    main()
