# Copy/paste guide for assignment Questions 1–16

**Important:** URLs in Q1/Q6 become valid only after the folder `EmotionDetection_Submission` is uploaded to `https://github.com/tsharma-dbr/Python` on the `main` branch. Terminal output and screenshots must be collected from actual runs, not guessed.

| Question | What to submit | File in this package |
|---|---|---|
| 1 | Public URL to project `README.md` | `submission_files/Q1_README_URL.txt` |
| 2 | Initial `emotion_detector` code that calls Watson NLP and returns JSON | `submission_files/2a_emotion_detection.py` |
| 3 | Actual terminal output proving import and a successful API test | Run commands in `submission_files/2b_application_creation_command.txt`; live Watson output is not fabricated here |
| 4 | Formatted function returning all five emotion scores and `dominant_emotion` | `submission_files/3a_output_formatting.py` |
| 5 | Actual terminal output of formatted function | `submission_files/3b_formatted_output_test_command.txt` |
| 6 | Public URL to package `__init__.py` | `submission_files/Q6_init_py_URL.txt` |
| 7 | Package validation terminal output | `submission_files/4b_packaging_test_command.txt` |
| 8 | Five course-style tests against the live Watson endpoint | `submission_files/5a_unit_testing.py` |
| 9 | Actual terminal output of the five live tests (requires a reachable endpoint) | `submission_files/5b_unit_testing_result_command.txt`; do not use the offline mock output |
| 10 | Flask deployment code | `submission_files/6a_server.py` |
| 11 | Genuine screenshot of the running app and result, named `6b_deployment_test.png` | Follow `evidence_instructions/Q11_6b_deployment_test.txt` |
| 12 | Emotion detector with HTTP 400 handling | `submission_files/7a_error_handling_function.py` |
| 13 | Flask server handling blank input | `submission_files/7b_error_handling_server.py` |
| 14 | Genuine screenshot showing blank-input validation, named `7c_error_handling_interface.png` | Follow `evidence_instructions/Q14_7c_error_handling_interface.txt` |
| 15 | Server code suitable for static analysis | `submission_files/8a_server_modified.py` |
| 16 | Real Pylint terminal output and score | `submission_files/8b_static_code_analysis_instructions.txt` |

The runnable project is at the package root: `EmotionDetection/`, `server.py`, `templates/index.html`, and `test_emotion_detection.py`.
