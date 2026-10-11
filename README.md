# IBM Watson NLP — Emotion Detection Application

## Project name
**Emotion Detection using IBM Watson NLP, Python, and Flask**

## Overview
This project sends text to the IBM Skills Network Watson NLP EmotionPredict endpoint, extracts the five emotion scores (anger, disgust, fear, joy, sadness), and identifies the dominant emotion. A small Flask web interface provides text submission and blank-input/service-error handling.

## Project files
- `EmotionDetection/emotion_detection.py` — API client and formatted result.
- `EmotionDetection/__init__.py` — package import.
- `server.py` — Flask routes and input validation.
- `templates/index.html` — web interface.
- `test_emotion_detection.py` — deterministic unit tests with mocked HTTP responses.
- `setup.py` and `requirements.txt` — package/dependency setup.

## Setup (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

## Run the unit tests
```powershell
py -m unittest -v test_emotion_detection.py
```

The unit tests mock the Watson endpoint so they can run offline. They test the output structure, dominant-emotion selection, HTTP 400 handling, and service errors. They do **not** establish that the live endpoint is reachable.

## Run the web application
```powershell
py server.py
```
Open `http://127.0.0.1:5000/` in a browser. Live analysis requires internet access to the IBM Skills Network endpoint. Blank-input validation can be tested without calling the endpoint.

## Packaging check
```powershell
py -c "from EmotionDetection import emotion_detector; print('EmotionDetection is a valid package')"
```

## Static analysis
```powershell
py -m pylint server.py
```
Paste the real terminal output and score into the assignment. Do not substitute an estimated score.

## Submission evidence
The course asks for screenshots of the running application and its blank-input validation. Capture those from the live app on your own computer and save them as `6b_deployment_test.png` and `7c_error_handling_interface.png`. The evidence images are not pre-fabricated in this source package.

## API endpoint
`https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict`

Header: `grpc-metadata-mm-model-id: emotion_aggregated-workflow_lang_en_stock`

## Course-style live API tests
`submission_files/5a_unit_testing.py` contains the five course-style tests that call the live Watson endpoint. Copy that file to the project root as `test_emotion_detection.py` to capture the assignment's live test output. The root `test_emotion_detection.py` in this package is a separate deterministic offline unit-test suite using mocks, included so local code behavior can be verified without an internet connection.
