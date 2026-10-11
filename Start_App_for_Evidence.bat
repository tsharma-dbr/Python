@echo off
setlocal
cd /d "%~dp0"
if not exist server.py (
  echo ERROR: Place this batch file in the EmotionDetection_Submission project root next to server.py.
  pause
  exit /b 1
)
echo Installing project dependencies...
py -m pip install -r requirements.txt
if errorlevel 1 (
  echo Dependency installation failed. Check internet access and Python/pip setup.
  pause
  exit /b 1
)
echo.
echo The Flask app will start at http://127.0.0.1:5000/
echo Use this app for both Q11 and Q14. Press Ctrl+C to stop it.
echo.
py server.py
pause
