"""Task 2: initial IBM Watson NLP EmotionPredict client.

This is the initial stage of the assignment: submit the service response JSON.
The later Task 3 activity formats the response into the five scores and the
name of the dominant emotion.
"""
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
