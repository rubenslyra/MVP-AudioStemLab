# RLLABS Audio Stem Lab

Projeto educacional para separar stems de áudio localmente usando Demucs.

## Portabilidade

O objetivo do projeto é evoluir para um aplicativo desktop instalável em Linux, Windows e macOS. Cada plataforma deve gerar seu próprio executável; não há um binário único universal para os três sistemas.

O app grava entradas, saídas, modelos e logs em diretórios de usuário próprios do sistema operacional, evitando depender da pasta onde o executável foi aberto.

Durante o desenvolvimento local, as entradas e saídas ficam nas pastas do projeto:

- `input_audio/`
- `output_stems/`

## Instalação de desenvolvimento

```bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip wheel
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Uso:

```bash
source .venv/bin/activate
python app.py
```

## Ambiente isolado do projeto

Para não depender do Python global, o projeto pode manter um Python gerenciado localmente em `.python/` e um virtualenv em `.venv311/`.

Uso:

```bash
source .venv311/bin/activate
python --version
python app.py
```

Esse ambiente não altera o Python do sistema.

## Separação suportada

O projeto usa Demucs como referência atual:

- `htdemucs`: voz, bateria, baixo e outros.
- `htdemucs` com `--two-stems vocals`: voz e instrumental.
- `htdemucs_6s`: voz, bateria, baixo, guitarra, piano/teclas e outros.

Ainda não há separação confiável para sopros, sintetizadores, voz principal e backing vocal. Esses casos devem ser tratados como evolução futura com modelos especializados, não como promessa do MVP atual.

Formatos de saída disponíveis:

- WAV
- MP3 320 kbps
- FLAC

## Build local

```bash
source .venv/bin/activate
pip install -r requirements-build.txt
pyinstaller packaging/AudioStemLab.spec
```

Para distribuição final, ainda é necessário adicionar pipeline por sistema operacional e empacotar `ffmpeg` ou oferecer instalação/download guiado na primeira execução.
