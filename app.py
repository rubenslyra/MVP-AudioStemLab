from core.terminal_ui import TerminalUI
from core.separator import AudioSeparator
from core.file_manager import FileManager


def main():
    ui = TerminalUI()
    manager = FileManager()
    separator = AudioSeparator()

    ui.clear()
    ui.header()

    manager.ensure_directories()
    ui.info(f"Pasta de entrada: {manager.input_dir}")
    ui.info(f"Pasta de saida: {manager.output_dir}")

    while True:
        ui.menu()

        option = input("\nEscolha uma opção: ").strip()

        if option == "1":
            audio_path = input("\nInforme o caminho do arquivo de áudio: ").strip()

            if not manager.file_exists(audio_path):
                ui.error("Arquivo não encontrado.")
                continue

            mode = ui.choose_separation_mode()
            output_format = ui.choose_output_format()

            ui.info("Iniciando separação. Em computadores mais simples, isso pode demorar.")

            try:
                separator.separate(audio_path, mode, output_format)
                ui.success(f"Separação concluída. Verifique a pasta {manager.output_dir}")
            except Exception as error:
                ui.error(f"Ocorreu um erro: {error}")

        elif option == "2":
            ui.info("Use apenas arquivos próprios, autorizados, Creative Commons ou domínio público.")
            url = input("\nURL do áudio/vídeo autorizado: ").strip()

            try:
                manager.download_audio(url)
                ui.success(f"Download concluído. Verifique a pasta {manager.input_dir}")
            except Exception as error:
                ui.error(f"Erro no download: {error}")

        elif option == "3":
            ui.about()

        elif option == "0":
            confirm = input("\nDeseja realmente sair? [s/n]: ").strip().lower()
            if confirm == "s":
                ui.goodbye()
                break

        else:
            ui.error("Opção inválida.")


if __name__ == "__main__":
    main()
