# Build on each target OS:
# pyinstaller --clean --noconfirm packaging/AudioStemLab.spec

from pathlib import Path

from PyInstaller.utils.hooks import collect_all


ROOT = Path(SPECPATH).resolve().parents[0]

datas = []
binaries = []
hiddenimports = []
hiddenimports += [
    "tkinter",
    "tkinter.filedialog",
    "rich",
]

datas += [
    (str(ROOT / "README.md"), "."),
    (str(ROOT / "VERSION"), "."),
    (str(ROOT / "CHANGELOG.md"), "."),
    (str(ROOT / "assets" / "brand" / "banner.png"), "assets/brand"),
    (str(ROOT / "assets" / "fonts" / "fira-code" / "ttf" / "*.ttf"), "assets/fonts/fira-code/ttf"),
    (str(ROOT / "assets" / "licenses" / "FIRA_CODE_LICENSE"), "assets/licenses"),
]

for package_name in ("demucs", "torch", "torchaudio", "torchcodec", "yt_dlp"):
    package_datas, package_binaries, package_hiddenimports = collect_all(package_name)
    datas += package_datas
    binaries += package_binaries
    hiddenimports += package_hiddenimports


a = Analysis(
    [str(ROOT / "app.py")],
    pathex=[str(ROOT)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "spleeter",
        "tensorflow",
        "pytest",
        "tests",
        "torch.testing",
        "torch.testing._internal",
        "torch.distributed",
        "torch._dynamo",
        "torch._inductor",
        "torch._export",
        "torch.onnx",
        "torch.utils.tensorboard",
        "torch.utils.benchmark",
    ],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="AudioStemLab",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="AudioStemLab",
)
