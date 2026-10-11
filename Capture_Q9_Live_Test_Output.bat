@echo off
setlocal
cd /d "%~dp0"
if not exist submission_files mkdir submission_files
set OUT=submission_files\5b_unit_testing_result.txt
echo Command: py -m unittest -v test_emotion_detection.py > "%OUT%"
echo. >> "%OUT%"
py -m unittest -v test_emotion_detection.py >> "%OUT%" 2>&1
set RC=%ERRORLEVEL%
type "%OUT%"
echo.
echo Exit code: %RC%
echo Paste the complete test output into Question 9 only when all five tests pass and the summary says OK.
pause
exit /b %RC%
