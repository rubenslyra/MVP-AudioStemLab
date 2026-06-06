# Application Snapshots

These snapshots document the current tester-facing flow of RLLABS Audio Stem Lab.

They are generated as SVG files so they remain readable in GitHub documentation and do not depend on a local terminal theme.

## 1. Home Screen

The first screen keeps the product identity, version, target desktop platforms, terminal information, and the main menu visible.

![Home screen](screenshots/01-home.svg)

## 2. File And Output Selection

The application is designed for non-technical testers. It opens native system dialogs for choosing the source audio file and output folder, with a manual fallback if dialogs are not available.

![File and output selection](screenshots/02-file-and-output-selection.svg)

## 3. Separation Options

The user chooses the separation mode and output format before processing starts.

![Separation options](screenshots/03-separation-options.svg)

## 4. Processing Progress

The raw Demucs progress output is converted into friendlier progress messages with whole percentages and elapsed time.

![Processing progress](screenshots/04-processing-progress.svg)

## 5. Release Packages

The release process provides CPU packages for broad compatibility and CUDA packages for compatible NVIDIA systems.

![Release packages](screenshots/05-release-packages.svg)

## Regenerating Snapshots

```bash
source .venv311/bin/activate
python scripts/generate_snapshots.py
```
