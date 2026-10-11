# Corrected resubmission guide — Questions 1–16

This guide is based on the uploaded `Feedback02(1).html`. The feedback awarded points to Q4, Q5, Q8, Q10, Q12, Q13, Q15 and Q16; avoid changing those answers unless you change the corresponding code. The missed points were Q1, Q2, Q3, Q6, Q7, Q9, Q11 and Q14.

## Q1 — README URL

First upload the complete `EmotionDetection_Submission` directory to the `main` branch of your public repository. The directory was not present in the repository when the supplied feedback was graded, so the earlier URL could not be verified. After commit, submit:

`https://github.com/tsharma-dbr/Python/blob/main/EmotionDetection_Submission/README.md`

## Q2 — `2a_emotion_detection`

Use `submission_files/2a_emotion_detection.py`. This is the **initial** Task 2 function: it calls the specified Watson NLP URL with the model header and raw-document payload and returns the JSON response. Do not use the later formatted-score implementation for this initial task; formatting belongs to Q4.

```python
import requests

def emotion_detector(text_to_analyze):
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
```

## Q3 — `2b_application_creation` terminal output

The feedback specifically says your previous answer used a package import and mocked output. From the course project directory, launch the Python shell, import with the required initial-stage import, and execute the live function:

```text
$ cd /home/project/final_project
$ python3
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I am so happy I am doing this.")
```

Paste the **actual dictionary returned by your run**, then the shell exit. Do not paste the placeholder or mocked output. The endpoint must be reachable for this to count as a live test. The compatibility module `emotion_detection.py` is also included in the project package.

## Q4 — `3a_output_formatting`

Use `submission_files/3a_output_formatting.py`. This answer already scored 1/1 in your feedback; keep the five scores (`anger`, `disgust`, `fear`, `joy`, `sadness`) and `dominant_emotion` in the returned dictionary.

## Q5 — `3b_formatted_output_test`

This answer already scored 1/1. Retain the successful formatted-output test. A mocked score dictionary was accepted for this question in your feedback, but label mock results accurately.

## Q6 — `__init__.py` URL

First upload/commit the directory so this file exists publicly. Then submit:

`https://github.com/tsharma-dbr/Python/blob/main/EmotionDetection_Submission/EmotionDetection/__init__.py`

The file imports the package function using `from .emotion_detection import emotion_detector`.

## Q7 — `4b_packaging_test` terminal output

The previous answer lost the point because it only said “EmotionDetection is a valid package”. Run this from the project root and paste the actual command plus the returned dictionary:

```text
$ python -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))"
{'anger': <actual score>, 'disgust': <actual score>, 'fear': <actual score>, 'joy': <actual score>, 'sadness': <actual score>, 'dominant_emotion': 'anger'}
```

The values in angle brackets are instructions, **not literal output**. Replace them with the actual values. The dominant emotion for the specified sentence should be `anger`.

## Q8 — `5a_unit_testing`

Your unit-test code scored 1/1. Keep the five live API tests for joy, anger, disgust, sadness, and fear in `submission_files/5a_unit_testing.py`.

## Q9 — `5b_unit_testing_result` terminal output

The feedback says your previous response supplied only a command, not a run result. In an environment that can reach the Watson endpoint, run from the project root:

```text
$ python -m unittest -v test_emotion_detection.py
```

Paste the complete **actual terminal output**. It must list all five tests as `ok` and end with `Ran 5 tests ...` and `OK`. Do not submit a command-only answer or offline mock-test output as evidence of five live tests.

## Q10 — `6a_server`

Your Flask server code scored 1/1. Keep `submission_files/6a_server.py` (or the equivalent working `server.py` in the project root).

## Q11 — `6b_deployment_test.png`

Upload a genuine browser screenshot of the running application **after a successful non-empty emotion analysis**. It should visibly include the app title, the submitted sentence, the emotion-score table, and the dominant emotion. Use a sentence such as `I am very happy today.`; wait for the actual result before capturing. Save as `6b_deployment_test.png`. A screenshot of a terminal, an empty form, a code editor, or an API error will not demonstrate successful deployment.

## Q12 — `7a_error_handling_function`

Your error-handling function scored 1/1. Keep `submission_files/7a_error_handling_function.py`; it should return the six expected keys with `None` values for HTTP 400 responses.

## Q13 — `7b_error_handling_server`

Your blank-input server logic scored 1/1. Keep `submission_files/7b_error_handling_server.py`.

## Q14 — `7c_error_handling_interface.png`

Upload a genuine browser screenshot of the app after blank input has been submitted and the page displays the validation message:

`Invalid input! Please enter some text to analyze.`

The screenshot should show the application interface and message together. Save it as `7c_error_handling_interface.png`. Do not upload the instructions, a command window, or a mockup.

## Q15 — `8a_server_modified`

Your modified server code scored 1/1. Keep `submission_files/8a_server_modified.py`.

## Q16 — `8b_static_code_analysis`

Your submitted Pylint output already scored 1/1. The feedback records:

```text
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

Retain this exact output if `server.py` has not changed since that run. If it has changed, rerun Pylint and paste the new actual output.

---

## Before retaking

1. Upload and commit the `EmotionDetection_Submission` folder to GitHub before using the Q1/Q6 links.
2. Run the live commands for Q3, Q7 and Q9 from a machine that can reach the IBM Skills Network Watson NLP endpoint; paste their real output.
3. Capture Q11 and Q14 from the actual app in a browser, not from an editor or terminal.

These corrections address the issues identified in the feedback, but the score depends on the grader and on providing real runtime evidence.
