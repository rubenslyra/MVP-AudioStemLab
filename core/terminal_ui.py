import os
import time


class TerminalUI:
    def clear(self):
        os.system("clear" if os.name != "nt" else "cls")

    def header(self):
        print("=" * 70)
        print(" RLLABS AUDIO STEM LAB ".center(70, "="))
        print("=" * 70)
        print(" Laboratório educacional de separação de áudio por IA")
        print(" Uso recomendado: arquivos próprios, autorizados ou Creative Commons")
        print("=" * 70)

    def menu(self):
        print("\n[1] Separar áudio local")
        print("[2] Baixar áudio autorizado com yt-dlp")
        print("[3] Sobre o projeto")
        print("[0] Sair")

    def choose_separation_mode(self):
        print("\nModo de separação:")
        print("[1] Voz + instrumental")
        print("[2] Voz + bateria + baixo + outros")
        print("[3] Voz + bateria + baixo + guitarra + piano/teclas + outros")
        print("\nObservação: sopros, sintetizadores e backing vocals ainda ficam em 'outros' ou 'voz'.")

        option = input("\nEscolha o modo: ").strip()

        if option == "1":
            return "vocals"
        if option == "3":
            return "extended6"
        return "full4"

    def choose_output_format(self):
        print("\nFormato de saída:")
        print("[1] WAV (padrão, maior qualidade)")
        print("[2] MP3 320 kbps")
        print("[3] FLAC")

        option = input("\nEscolha o formato: ").strip()

        if option == "2":
            return "mp3"
        if option == "3":
            return "flac"
        return "wav"

    def info(self, message):
        print(f"\n[INFO] {message}")

    def success(self, message):
        print(f"\n[OK] {message}")

    def error(self, message):
        print(f"\n[ERRO] {message}")

    def about(self):
        print("\nRLLabs Audio Stem Lab")
        print("Projeto didático para estudo de IA aplicada à música.")
        print("Primeiro objetivo: separar stems e compreender entrada, processamento e saída.")
        print("Próxima evolução: interface visual, análise de waveform e comparação entre modelos.")

    def goodbye(self):
        print("\nEncerrando o laboratório...")
        for number in range(3, 0, -1):
            print(f"Fechando em {number}...")
            time.sleep(1)
        print("Programa finalizado com segurança.")
