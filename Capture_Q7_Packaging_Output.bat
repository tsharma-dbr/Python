@echo off
setlocal
cd /d "%~dp0"
py -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))"
echo.
echo Paste the import command and the REAL dictionary above into Question 7 only if the live API returned emotion scores and dominant_emotion is anger.
pause
