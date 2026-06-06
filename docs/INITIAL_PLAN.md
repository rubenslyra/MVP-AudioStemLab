rllabs-audio-stem-lab/
│
├── app.py
├── requirements.txt
│
├── input_audio/
│   └── coloque_aqui_suas_musicas_autorizadas.txt
│
├── output_stems/
│
├── core/
│   ├── __init__.py
│   ├── separator.py
│   ├── file_manager.py
│   └── terminal_ui.py
│
└── docs/
    └── README.md

-----

Perfeito, Rubens. Vamos iniciar como **projeto educacional de laboratório**, não como clone do Moises.

# Projeto inicial: **RLLabs Audio Stem Lab**

Objetivo do MVP:

> Criar uma aplicação local em Python que receba um arquivo de áudio autorizado, separe voz/instrumental ou voz/baixo/bateria/outros, organize os arquivos gerados e prepare a base para uma futura interface visual didática.

A stack inicial será:

| Camada                  | Escolha inicial | Motivo                                                                                                                                                                                                                                    |
| ----------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Separação de áudio      | **Demucs**      | Boa qualidade para stems como voz, bateria, baixo e outros. A versão v4 usa Hybrid Transformer Demucs, mas o repositório original informa que não está mais ativamente mantido. Ainda serve bem para protótipo/laboratório. ([GitHub][1]) |
| Alternativa comparativa | **Spleeter**    | Mais clássico, rápido e didático; suporta 2, 4 e 5 stems, com modelos pré-treinados. Usa Python + TensorFlow. ([GitHub][2])                                                                                                               |
| Download opcional       | **yt-dlp**      | Apenas para materiais próprios, autorizados, Creative Commons ou domínio público. O projeto suporta milhares de sites e pode ser usado via linha de comando. ([GitHub][3])                                                                |
| Dataset de estudo       | **MoisesDB**    | Útil para pesquisa não comercial; está sob licença CC BY-NC-SA 4.0. ([GitHub][4])                                                                                                                                                         |

---

# Fase 1 — MVP de terminal

## Estrutura do projeto

```text
rllabs-audio-stem-lab/
│
├── app.py
├── requirements.txt
│
├── input_audio/
│   └── coloque_aqui_suas_musicas_autorizadas.txt
│
├── output_stems/
│
├── core/
│   ├── __init__.py
│   ├── separator.py
│   ├── file_manager.py
│   └── terminal_ui.py
│
└── docs/
    └── README.md
```

---

# Instalação inicial no Ubuntu

Use preferencialmente Python 3.10 ou 3.11 para reduzir dor de cabeça com bibliotecas de áudio.

```bash
sudo apt update
sudo apt install -y ffmpeg python3-venv

mkdir rllabs-audio-stem-lab
cd rllabs-audio-stem-lab

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip wheel
pip install demucs yt-dlp
```

Crie o arquivo `requirements.txt`:

```txt
demucs
yt-dlp
```

---

# Código inicial

## `app.py`

```python
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

    while True:
        ui.menu()

        option = input("\nEscolha uma opção: ").strip()

        if option == "1":
            audio_path = input("\nInforme o caminho do arquivo de áudio: ").strip()

            if not manager.file_exists(audio_path):
                ui.error("Arquivo não encontrado.")
                continue

            mode = ui.choose_separation_mode()

            ui.info("Iniciando separação. Em computadores mais simples, isso pode demorar.")

            try:
                separator.separate(audio_path, mode)
                ui.success("Separação concluída. Verifique a pasta output_stems/")
            except Exception as error:
                ui.error(f"Ocorreu um erro: {error}")

        elif option == "2":
            ui.info("Use apenas arquivos próprios, autorizados, Creative Commons ou domínio público.")
            url = input("\nURL do áudio/vídeo autorizado: ").strip()

            try:
                manager.download_audio(url)
                ui.success("Download concluído. Verifique a pasta input_audio/")
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
```

---

## `core/terminal_ui.py`

```python
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

        option = input("\nEscolha o modo: ").strip()

        if option == "1":
            return "vocals"
        return "full"

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
```

---

## `core/file_manager.py`

```python
import os
import subprocess
from pathlib import Path


class FileManager:
    def __init__(self):
        self.input_dir = Path("input_audio")
        self.output_dir = Path("output_stems")

    def ensure_directories(self):
        self.input_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True)

    def file_exists(self, path):
        return Path(path).is_file()

    def download_audio(self, url):
        command = [
            "yt-dlp",
            "-x",
            "--audio-format",
            "mp3",
            "-o",
            "input_audio/%(title)s.%(ext)s",
            url
        ]

        subprocess.run(command, check=True)
```

---

## `core/separator.py`

```python
import subprocess
from pathlib import Path


class AudioSeparator:
    def __init__(self):
        self.output_dir = Path("output_stems")

    def separate(self, audio_path, mode):
        if mode == "vocals":
            command = [
                "python",
                "-m",
                "demucs",
                "--two-stems",
                "vocals",
                "-o",
                str(self.output_dir),
                audio_path
            ]
        else:
            command = [
                "python",
                "-m",
                "demucs",
                "-o",
                str(self.output_dir),
                audio_path
            ]

        subprocess.run(command, check=True)
```

---

# Como testar

Coloque um arquivo `.mp3` ou `.wav` autorizado dentro de:

```text
input_audio/
```

Depois rode:

```bash
source .venv/bin/activate
python app.py
```

Escolha:

```text
[1] Separar áudio local
```

E informe, por exemplo:

```text
input_audio/minha_musica.mp3
```

O resultado deve aparecer em:

```text
output_stems/
```

---

# Observação importante para o seu computador

Como seu processador é um **i3-4150 com 2 núcleos e 4 threads**, comece com:

1. músicas curtas;
2. testes de 30 segundos a 1 minuto;
3. modo “voz + instrumental” primeiro;
4. sem interface gráfica no começo.

A primeira vitória técnica do projeto é esta:

> entrada de áudio → processamento por modelo de IA → saída organizada em stems.

Depois disso, a gente evolui para:

> waveform visual, player por stem, botão de mute/solo, comparação entre Demucs e Spleeter, e uma camada didática para mostrar aos alunos o que entrou, o que foi processado e o que saiu.

[1]: https://github.com/facebookresearch/demucs "GitHub - facebookresearch/demucs: Code for the paper Hybrid Spectrogram and Waveform Source Separation · GitHub"
[2]: https://github.com/deezer/spleeter "GitHub - deezer/spleeter: Deezer source separation library including pretrained models. · GitHub"
[3]: https://github.com/yt-dlp/yt-dlp "GitHub - yt-dlp/yt-dlp: A feature-rich command-line audio/video downloader · GitHub"
[4]: https://github.com/moises-ai/moises-db "GitHub - moises-ai/moises-db: Moises Source Separation Public Dataset · GitHub"
