@echo off
setlocal
cd /d "%~dp0"
echo ================================================
echo Question 14 - Error-handling screenshot helper
echo ================================================
python -c "import flask" >nul 2>&1
if errorlevel 1 (
  echo Flask is not installed in the selected Python environment.
  echo Open Command Prompt in this folder and run:
  echo   python -m pip install -r requirements.txt
  echo Then run this file again.
  pause
  exit /b 1
)
start "Emotion Detection Flask Server" cmd /k "cd /d ""%~dp0"" && python server.py"
timeout /t 4 /nobreak >nul
start "" "http://127.0.0.1:5000/emotionDetector?textToAnalyze="
echo.
echo The browser should show the application's blank-input error message.
echo Capture the browser using Win+Shift+S and save it as:
echo   7c_error_handling_interface.png
 echo Upload that PNG to Question 14.
pause
endlocal
