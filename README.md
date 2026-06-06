<p align="center">
  <img src="assets/brand/banner.png" alt="RLLABS Audio Stem Lab" width="240">
</p>

<h1 align="center">RLLABS Audio Stem Lab</h1>

<p align="center">
  Separacao local de stems de audio com IA, criada como MVP educacional e base para um aplicativo desktop portavel.
</p>

<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-0.3.4-0f766e?style=for-the-badge">
  <img alt="Python" src="https://img.shields.io/badge/python-3.10%20%7C%203.11-1f2937?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Platforms" src="https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-334155?style=for-the-badge">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-111827?style=for-the-badge">
</p>

<p align="center">
  <img alt="Demucs" src="https://img.shields.io/badge/audio-Demucs-2563eb?style=flat-square">
  <img alt="Output" src="https://img.shields.io/badge/output-WAV%20%7C%20MP3%20%7C%20FLAC-475569?style=flat-square">
  <img alt="Desktop only" src="https://img.shields.io/badge/mobile-not%20available-7f1d1d?style=flat-square">
</p>

---

## Visao Geral

O **RLLABS Audio Stem Lab** e uma aplicacao local para separar faixas de audio em stems usando modelos de IA. A versao atual ainda e um MVP de terminal, mas ja foi estruturada para evoluir para um aplicativo desktop instalavel e portavel.

O projeto prioriza:

- execucao local;
- experiencia simples para testadores;
- organizacao clara de entradas e saidas;
- compatibilidade futura com Linux, Windows e macOS;
- cuidado tecnico com os limites reais dos modelos de separacao.

## Estado Da Versao

| Item | Status |
| --- | --- |
| Versao atual | `0.3.4` |
| Interface | Terminal assistido |
| Plataformas alvo | Linux, Windows e macOS |
| Mobile | Ainda nao disponivel |
| Separador principal | Demucs |
| Build desktop | Scaffold com PyInstaller |

## Funcionalidades

- Separacao local de audio com Demucs.
- Seletor nativo de arquivo de origem.
- Seletor nativo de pasta de destino.
- Terminal estilizado com cabecalho persistente.
- Mensagens de progresso mais legiveis.
- Saida em `output_stems/` durante desenvolvimento.
- Download opcional com `yt-dlp` para materiais autorizados.
- Fonte Fira Code v6.2 incluida no pacote de assets.
- Launchers auxiliares para Linux, Windows e macOS.

## Modos De Separacao

| Modo | Modelo | Stems esperados |
| --- | --- | --- |
| Voz + instrumental | `htdemucs` com `--two-stems vocals` | voz, instrumental |
| Separacao padrao | `htdemucs` | voz, bateria, baixo, outros |
| Separacao estendida | `htdemucs_6s` | voz, bateria, baixo, guitarra, piano/teclas, outros |

### Limites Tecnicos

Sopros, sintetizadores, teclado detalhado, voz principal e backing vocal ainda nao sao stems confiaveis nesta base. Esses casos exigem pesquisa com modelos especializados ou etapas adicionais de classificacao.

## Formatos De Saida

- WAV
- MP3 320 kbps
- FLAC

## Estrutura Principal

```text
MVP-AudioStemLab/
├── app.py
├── core/
│   ├── file_dialogs.py
│   ├── file_manager.py
│   ├── paths.py
│   ├── separator.py
│   ├── terminal_ui.py
│   └── version.py
├── input_audio/
├── output_stems/
├── launchers/
├── packaging/
├── assets/
└── docs/
```

## Instalacao Para Desenvolvimento

Use preferencialmente Python `3.10` ou `3.11`.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel
pip install -r requirements.txt
pip install -r requirements-dev.txt
python app.py
```

### Ambiente Isolado Local

Este workspace tambem pode usar o ambiente isolado ja preparado:

```bash
source .venv311/bin/activate
python --version
python app.py
```

## Uso

1. Execute o aplicativo:

```bash
python app.py
```

2. Escolha `Separar audio local`.
3. Selecione o arquivo pelo gerenciador de arquivos do sistema.
4. Escolha o modo de separacao.
5. Escolha o formato de saida.
6. Escolha a pasta de destino ou use `output_stems/`.

## Launchers

Arquivos auxiliares para teste por sistema:

```text
launchers/audiostemlab-linux.sh
launchers/audiostemlab-linux.desktop
launchers/audiostemlab-macos.command
launchers/audiostemlab-windows.bat
```

## Build De Executavel

O build precisa ser gerado separadamente em cada sistema operacional de destino.

```bash
source .venv/bin/activate
pip install -r requirements-build.txt
pyinstaller packaging/AudioStemLab.spec
```

O binario sera criado em `dist/`.

## Assets De Fonte

O projeto inclui Fira Code v6.2 em:

```text
assets/fonts/fira-code/ttf/
```

A fonte e fornecida sob SIL Open Font License 1.1. A licenca esta em:

```text
assets/licenses/FIRA_CODE_LICENSE
```

A ativacao real da fonte e das ligaduras depende do terminal ou do instalador em cada sistema operacional.

## Testes

```bash
source .venv311/bin/activate
python -m pytest -q
```

Resultado esperado na versao atual:

```text
7 passed
```

## Releases

- `v0.1.0`: MVP CLI inicial.
- `v0.3.4`: experiencia de terminal para testadores, seletores nativos, fonte Fira Code e progresso mais legivel.

Notas completas:

```text
docs/releases/
```

## Roadmap Curto

- Organizar jobs por musica.
- Salvar logs de processamento.
- Melhorar mensagens de erro para usuario comum.
- Preparar instaladores por sistema operacional.
- Reduzir peso do runtime com build CPU-only.
- Evoluir para interface desktop completa.

## Licenca

Este projeto esta sob a licenca MIT. Consulte [LICENSE](LICENSE).
