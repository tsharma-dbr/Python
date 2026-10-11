@echo off
setlocal
cd /d "%~dp0.."
if not exist submission_files mkdir submission_files
set OUT=submission_files\2b_application_creation.txt
echo Project directory: %CD% > "%OUT%"
echo Command: py -c "from emotion_detection import emotion_detector; print(emotion_detector('I love this new technology'))" >> "%OUT%"
echo. >> "%OUT%"
py -c "from emotion_detection import emotion_detector; print(emotion_detector('I love this new technology'))" >> "%OUT%" 2>&1
set RC=%ERRORLEVEL%
echo. >> "%OUT%"
echo Exit code: %RC% >> "%OUT%"
type "%OUT%"
echo.
echo Paste this REAL output into Question 3 only if the API call succeeded.
pause
exit /b %RC%
