# RLLABS Audio Stem Lab

Projeto educacional (MVP) para separar stems de áudio localmente usando Demucs.

## Instalação para desenvolvimento

Use Python 3.10 ou 3.11 para reduzir problemas com bibliotecas de áudio e ML.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel
pip install -r requirements.txt
pip install -r requirements-dev.txt
python app.py
```

Este workspace também pode usar um Python isolado baixado pelo `uv`:

```bash
source .venv311/bin/activate
python --version
python app.py
```

O aplicativo usa pastas de dados do usuário, em vez de depender do diretório atual:

- Em desenvolvimento: `input_audio/` e `output_stems/` dentro do projeto.
- Em executável empacotado no futuro:
  - Linux: `~/.local/share/AudioStemLab`
  - Windows: `%APPDATA%\AudioStemLab`
  - macOS: `~/Library/Application Support/AudioStemLab`

## Modos de separação

- Voz + instrumental: modelo `htdemucs` com `--two-stems vocals`.
- Voz + bateria + baixo + outros: modelo `htdemucs`.
- Voz + bateria + baixo + guitarra + piano/teclas + outros: modelo `htdemucs_6s`.

Sopros, sintetizadores, teclado detalhado, voz principal e backing vocal ainda não são stems confiáveis nesta base. Eles precisam de modelos adicionais ou uma etapa posterior de classificação/separação fina.

## Formatos de saída

- WAV
- MP3 320 kbps
- FLAC

## Build de executável

O build precisa ser gerado em cada sistema operacional de destino.

```bash
source .venv/bin/activate
pip install -r requirements-build.txt
pyinstaller packaging/AudioStemLab.spec
```

O binário será criado em `dist/`.
