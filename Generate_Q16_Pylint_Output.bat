@echo off
setlocal
cd /d "%~dp0"
if not exist server.py (
  echo ERROR: Place this batch file in the EmotionDetection_Submission project root next to server.py.
  pause
  exit /b 1
)
if not exist submission_files mkdir submission_files
echo Installing Pylint...
py -m pip install pylint
if errorlevel 1 (
  echo ERROR: Pylint could not be installed. Check internet access and pip configuration.
  pause
  exit /b 1
)
echo Running Pylint on server.py and saving the complete output...
py -m pylint server.py > submission_files\8b_static_code_analysis.txt 2>&1
set PYLINT_EXIT=%ERRORLEVEL%
echo.
echo ===== Actual Pylint output =====
type submission_files\8b_static_code_analysis.txt
echo.
echo Saved to: %CD%\submission_files\8b_static_code_analysis.txt
echo Pylint exit code: %PYLINT_EXIT% (nonzero may indicate lint findings; review the output and score)
pause
