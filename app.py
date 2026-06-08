from core.terminal_ui import TerminalUI
from core.separator import AudioSeparator
from core.file_manager import FileManager
from core.file_dialogs import FileDialogUnavailable, choose_audio_file, choose_output_folder


def main():
    ui = TerminalUI()
    manager = FileManager()
    separator = AudioSeparator()

    manager.ensure_directories()

    while True:
        ui.refresh()
        ui.menu()

        option = ui.ask("Escolha uma opcao", default="1").strip()

        if option == "1":
            ui.refresh()
            source_method = ui.choose_audio_source_method()
            if source_method == "1":
                try:
                    selected = choose_audio_file(manager.input_dir)
                    if not selected:
                        ui.warning("Nenhum arquivo selecionado.")
                        ui.wait()
                        continue
                    audio_path = str(selected)
                except FileDialogUnavailable as error:
                    ui.warning(str(error))
                    audio_path = ui.ask("Informe o caminho do arquivo de audio").strip()
            else:
                audio_path = ui.ask("Informe o caminho do arquivo de audio").strip()

            if not manager.file_exists(audio_path):
                ui.error("Arquivo não encontrado.")
                ui.wait()
                continue

            ui.refresh()
            mode = ui.choose_separation_mode()
            output_format = ui.choose_output_format()
            output_dir = manager.output_dir

            if ui.choose_destination_method() == "2":
                try:
                    selected_dir = choose_output_folder(
                        manager.output_dir,
                        title="Escolha a pasta de destino dos stems",
                    )
                    if selected_dir:
                        output_dir = selected_dir
                    else:
                        ui.warning("Nenhuma pasta selecionada. Usando a pasta padrao.")
                except FileDialogUnavailable as error:
                    ui.warning(str(error))
                    output_dir = ui.ask("Informe a pasta de destino", default=str(manager.output_dir)).strip()

            ui.refresh()
            ui.info("Iniciando separação. Em computadores mais simples, isso pode demorar.")
            ui.info(f"Arquivo de origem: {audio_path}")
            ui.info(f"Pasta de destino: {output_dir}")

            try:
                last_message = {"value": None}

                def show_progress(message):
                    if message and message != last_message["value"]:
                        last_message["value"] = message
                        ui.info(message)

                separator.separate(audio_path, mode, output_format, output_dir, show_progress)
                ui.success(f"Separação concluída. Verifique a pasta {output_dir}")
            except Exception as error:
                ui.error(f"Ocorreu um erro: {error}")
            ui.wait()

        elif option == "2":
            ui.refresh()
            ui.info("Use apenas arquivos próprios, autorizados, Creative Commons ou domínio público.")
            url = ui.ask("URL do audio/video autorizado").strip()
            download_dir = manager.input_dir

            if ui.choose_download_destination_method() == "2":
                try:
                    selected_dir = choose_output_folder(
                        manager.input_dir,
                        title="Escolha a pasta para salvar o download",
                    )
                    if selected_dir:
                        download_dir = selected_dir
                    else:
                        ui.warning("Nenhuma pasta selecionada. Usando a pasta padrao do aplicativo.")
                except FileDialogUnavailable as error:
                    ui.warning(str(error))
                    download_dir = ui.ask("Informe a pasta para salvar o download", default=str(manager.input_dir)).strip()

            try:
                ui.refresh()
                ui.info(f"Baixando audio autorizado em: {download_dir}")
                manager.download_audio(url, download_dir)
                ui.success(f"Download concluído. Verifique a pasta {download_dir}")
            except Exception as error:
                ui.error(f"Erro no download: {error}")
            ui.wait()

        elif option == "3":
            ui.refresh()
            ui.about()
            ui.wait()

        elif option == "0":
            if ui.confirm("Deseja realmente sair?"):
                ui.goodbye()
                break

        else:
            ui.error("Opção inválida.")
            ui.wait()


if __name__ == "__main__":
    main()
