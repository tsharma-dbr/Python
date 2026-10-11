Evidence items must be captured from the actual running application; the package does not include fabricated screenshots or fabricated live API logs.

Q11 / 6b_deployment_test.png:
- Run `py -m pip install -r requirements.txt` and then `py server.py`.
- Open http://127.0.0.1:5000/.
- Enter `I am very happy today.` and click Analyze emotion.
- Wait until the results panel shows all five emotion scores and the dominant emotion.
- Capture the browser window with Win+Shift+S and save as `6b_deployment_test.png`.
- If a 502/service error appears, fix network/API access first; an error screenshot will not show successful deployment.

Q14 / 7c_error_handling_interface.png:
- Keep the Flask app running.
- In the browser, open http://127.0.0.1:5000/.
- Leave the Text to analyze field blank and click Analyze emotion.
- Confirm the page shows `Invalid input! Please enter some text to analyze.`
- Capture the browser window with the validation message visible and save as `7c_error_handling_interface.png`.

Q3 / 2b_application_creation:
From `/home/project/final_project`, start `python3`, run `from emotion_detection import emotion_detector`, then call `emotion_detector("I am so happy I am doing this.")`. Paste the actual response and shell output.

Q7 / 4b_packaging_test:
From the project root, run:
`python -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))"`
Paste the actual dictionary showing all five scores and `dominant_emotion` as `anger`.

Q9 / 5b_unit_testing_result:
From the project root and on a machine that can reach the endpoint, run:
`python -m unittest -v test_emotion_detection.py`
Paste the complete output with five passing tests and `OK`.

Q1 and Q6:
Upload/commit this folder to the public repository on `main` before submitting URLs. The GitHub links cannot resolve until committed.
