# Build on each target OS:
# pyinstaller packaging/AudioStemLab.spec

from PyInstaller.utils.hooks import collect_all


datas = []
binaries = []
hiddenimports = []

datas += [
    ("assets/fonts/fira-code/ttf/*.ttf", "assets/fonts/fira-code/ttf"),
    ("assets/licenses/FIRA_CODE_LICENSE", "assets/licenses"),
]

for package_name in ("demucs", "torch", "torchaudio"):
    package_datas, package_binaries, package_hiddenimports = collect_all(package_name)
    datas += package_datas
    binaries += package_binaries
    hiddenimports += package_hiddenimports


a = Analysis(
    ["app.py"],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["spleeter", "tensorflow"],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
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
