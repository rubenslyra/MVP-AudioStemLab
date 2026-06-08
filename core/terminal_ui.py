from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table

from core.terminal_launcher import terminal_profile_summary
from core.version import APP_NAME, APP_VERSION, SUPPORTED_PLATFORMS


class TerminalUI:
    def __init__(self):
        self.console = Console()

    def clear(self):
        if self.console.is_terminal:
            self.console.file.write("\033[H\033[2J\033[3J")
            self.console.file.flush()
        else:
            self.console.clear()

    def header(self):
        profile = terminal_profile_summary()
        system = profile["system"]

        subtitle = (
            "Separacao local de stems por IA | "
            f"v{APP_VERSION} | Sistema: {system} | "
            f"Desktop: {', '.join(SUPPORTED_PLATFORMS)}"
        )
        self.console.print(
            Panel(
                f"[bold]RLLABS AUDIO STEM LAB[/bold]\n{subtitle}\n"
                f"Terminal: {profile['terminal']}\n"
                "Use apenas arquivos proprios, autorizados, Creative Commons ou dominio publico.",
                box=box.ROUNDED,
                border_style="cyan",
            )
        )

    def refresh(self):
        self.clear()
        self.header()

    def menu(self):
        table = Table(box=box.SIMPLE_HEAVY, show_header=False, padding=(0, 1))
        table.add_column("Opcao", style="cyan", no_wrap=True)
        table.add_column("Acao")
        table.add_row("1", "Separar audio local")
        table.add_row("2", "Baixar audio autorizado com yt-dlp")
        table.add_row("3", "Sobre o projeto")
        table.add_row("0", "Sair")
        self.console.print(table)

    def ask(self, message, default=None):
        return Prompt.ask(message, default=default)

    def confirm(self, message, default=False):
        return Confirm.ask(message, default=default)

    def choose_separation_mode(self):
        self.console.print("\n[bold]Modo de separacao[/bold]")
        self.console.print("[cyan]1[/cyan] Voz + instrumental")
        self.console.print("[cyan]2[/cyan] Voz + bateria + baixo + outros")
        self.console.print("[cyan]3[/cyan] Voz + bateria + baixo + guitarra + piano/teclas + outros")
        self.console.print(
            "[yellow]Nota:[/yellow] sopros, sintetizadores e backing vocals ainda ficam em 'outros' ou 'voz'."
        )

        option = self.ask("Escolha o modo", default="1").strip()

        if option == "1":
            return "vocals"
        if option == "3":
            return "extended6"
        return "full4"

    def choose_output_format(self):
        self.console.print("\n[bold]Formato de saida[/bold]")
        self.console.print("[cyan]1[/cyan] WAV - maior qualidade")
        self.console.print("[cyan]2[/cyan] MP3 - arquivo menor, 320 kbps")
        self.console.print("[cyan]3[/cyan] FLAC - alta qualidade com compressao")

        option = self.ask("Escolha o formato", default="1").strip()

        if option == "2":
            return "mp3"
        if option == "3":
            return "flac"
        return "wav"

    def show_paths(self, input_dir, output_dir):
        table = Table(title="Pastas do projeto", box=box.SIMPLE, show_lines=False)
        table.add_column("Tipo", style="cyan")
        table.add_column("Caminho")
        table.add_row("Entrada", str(input_dir))
        table.add_row("Saida padrao", str(output_dir))
        self.console.print(table)

    def choose_audio_source_method(self):
        self.console.print("\n[bold]Arquivo de origem[/bold]")
        self.console.print("[cyan]1[/cyan] Abrir seletor de arquivos")
        self.console.print("[cyan]2[/cyan] Digitar ou colar caminho manualmente")
        return self.ask("Escolha como informar o arquivo", default="1").strip()

    def choose_destination_method(self):
        self.console.print("\n[bold]Pasta de destino[/bold]")
        self.console.print("[cyan]1[/cyan] Usar pasta padrao output_stems")
        self.console.print("[cyan]2[/cyan] Escolher outra pasta")
        return self.ask("Escolha a pasta de destino", default="1").strip()

    def choose_download_destination_method(self):
        self.console.print("\n[bold]Pasta para salvar o download[/bold]")
        self.console.print("[cyan]1[/cyan] Usar pasta padrao do aplicativo")
        self.console.print("[cyan]2[/cyan] Escolher outra pasta")
        return self.ask("Escolha a pasta do download", default="1").strip()

    def info(self, message):
        self.console.print(f"\n[cyan]INFO[/cyan] {message}")

    def success(self, message):
        self.console.print(f"\n[green]OK[/green] {message}")

    def error(self, message):
        self.console.print(f"\n[red]ERRO[/red] {message}")

    def warning(self, message):
        self.console.print(f"\n[yellow]AVISO[/yellow] {message}")

    def wait(self):
        self.console.input("\nPressione Enter para continuar...")

    def about(self):
        self.console.print(
            Panel(
                f"[bold]{APP_NAME}[/bold]\n"
                f"Versao: {APP_VERSION}\n"
                "Projeto didatico para estudo de IA aplicada a musica.\n"
                "Plataformas desktop previstas: Linux, Windows e macOS.\n"
                "Mobile ainda nao esta disponivel nesta versao.\n\n"
                "Proxima evolucao: jobs organizados, logs, build CPU-only e interface desktop.",
                box=box.ROUNDED,
                border_style="cyan",
            )
        )

    def goodbye(self):
        self.clear()
