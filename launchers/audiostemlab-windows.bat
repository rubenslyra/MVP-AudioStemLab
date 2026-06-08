@echo off
setlocal
cd /d "%~dp0\.."

if exist "AudioStemLab\AudioStemLab.exe" (
  "AudioStemLab\AudioStemLab.exe"
  exit /b %ERRORLEVEL%
)

if exist ".venv311\Scripts\python.exe" (
  ".venv311\Scripts\python.exe" app.py
) else (
  python app.py
)
