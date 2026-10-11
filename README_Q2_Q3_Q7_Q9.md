# Corrections for Questions 2, 3, 7 and 9

This revision addresses the exact feedback in Feedback02(1).html:

- Q2: The Task 2 stage uses the reference-style `emotion_detector` that POSTs the specified URL/header/payload and returns `response.text` (raw JSON text), before Task 3 formatting.
- Q3: The required import is `from emotion_detection import emotion_detector`. The transcript must come from the Python shell in `/home/project/final_project` (or the equivalent local project root) and a real live request. Use `submission_files/2b_application_creation_command.txt` or run `Capture_Q3_Live_Output.bat` on Windows.
- Q7: Use exactly `from EmotionDetection.emotion_detection import emotion_detector` and print the scores for `I am really mad about this`. The dictionary must show all five emotions and `dominant_emotion: 'anger'`. Use `Capture_Q7_Packaging_Output.bat` on Windows.
- Q9: `test_emotion_detection.py` contains the five live tests from the assignment. Run `Capture_Q9_Live_Test_Output.bat` on Windows or `python -m unittest -v test_emotion_detection.py` in the lab. Paste the actual output with five `ok` results and final `OK`.

## Critical

Terminal output must be generated where the IBM Skills Network endpoint is reachable. This environment cannot resolve `sn-watson-emotion.labs.skills.network`, so no live scores or successful live test results have been fabricated. The files marked OUTPUT CAPTURE are templates until replaced with actual terminal output.
