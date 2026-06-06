<p align="center">
  <img src="assets/brand/banner.png" alt="RLLABS Audio Stem Lab" width="240">
</p>

<h1 align="center">RLLABS Audio Stem Lab</h1>

<p align="center">
  Local AI-powered audio stem separation, built as an educational MVP and foundation for a portable desktop application.
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

## Overview

**RLLABS Audio Stem Lab** is a local application for separating audio tracks into stems using AI models. The current release is still a terminal-based MVP, but the project is already structured to evolve into an installable and portable desktop application.

The project prioritizes:

- local execution;
- a simple experience for testers;
- clear input and output organization;
- future compatibility with Linux, Windows, and macOS;
- technical care around the real limits of source separation models.

## Release Status

| Item | Status |
| --- | --- |
| Current version | `0.3.4` |
| Interface | Assisted terminal |
| Target platforms | Linux, Windows, and macOS |
| Mobile | Not available yet |
| Main separator | Demucs |
| Desktop build | PyInstaller scaffold |

## Features

- Local audio separation with Demucs.
- Native file picker for source audio selection.
- Native folder picker for output destination selection.
- Styled terminal with persistent system header.
- Cleaner progress messages for non-technical users.
- Development output folder: `output_stems/`.
- Optional `yt-dlp` download flow for authorized material.
- Fira Code v6.2 bundled as a project asset.
- Helper launchers for Linux, Windows, and macOS.

## Separation Modes

| Mode | Model | Expected stems |
| --- | --- | --- |
| Vocals + instrumental | `htdemucs` with `--two-stems vocals` | vocals, instrumental |
| Standard separation | `htdemucs` | vocals, drums, bass, other |
| Extended separation | `htdemucs_6s` | vocals, drums, bass, guitar, piano/keys, other |

### Technical Limits

Brass, synthesizers, detailed keyboard layers, lead vocals, and backing vocals are not reliable standalone stems in the current model setup. These cases require specialized models or additional post-processing and classification steps.

## Output Formats

- WAV
- MP3 320 kbps
- FLAC

## Project Structure

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

## Development Setup

Python `3.10` or `3.11` is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel
pip install -r requirements.txt
pip install -r requirements-dev.txt
python app.py
```

### Local Isolated Environment

This workspace can also use the prepared isolated environment:

```bash
source .venv311/bin/activate
python --version
python app.py
```

## Usage

1. Run the application:

```bash
python app.py
```

2. Choose `Separate local audio`.
3. Select the source file using the system file picker.
4. Choose the separation mode.
5. Choose the output format.
6. Select a destination folder or use `output_stems/`.

## Launchers

Helper launchers for platform-specific testing:

```text
launchers/audiostemlab-linux.sh
launchers/audiostemlab-linux.desktop
launchers/audiostemlab-macos.command
launchers/audiostemlab-windows.bat
```

## Executable Build

Builds must be generated separately on each target operating system.

```bash
source .venv/bin/activate
pip install -r requirements-build.txt
pyinstaller packaging/AudioStemLab.spec
```

The executable will be created in `dist/`.

## Font Assets

The project includes Fira Code v6.2 at:

```text
assets/fonts/fira-code/ttf/
```

The font is distributed under the SIL Open Font License 1.1. The license is available at:

```text
assets/licenses/FIRA_CODE_LICENSE
```

Actual font and ligature activation depends on the terminal or installer used by each operating system.

## Tests

```bash
source .venv311/bin/activate
python -m pytest -q
```

Expected result for the current release:

```text
7 passed
```

## Releases

- `v0.1.0`: initial CLI MVP.
- `v0.3.4`: terminal experience for testers, native pickers, Fira Code assets, and cleaner progress output.

Full release notes:

```text
docs/releases/
```

## Short Roadmap

- Organize processing jobs by song.
- Save processing logs.
- Improve user-facing error messages.
- Prepare installers for each operating system.
- Reduce runtime weight with a CPU-only build path.
- Evolve into a complete desktop interface.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
