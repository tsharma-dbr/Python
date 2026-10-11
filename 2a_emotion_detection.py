import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

HEADERS = {
    'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
}


def emotion_detector(text_to_analyse: str) -> str:
    """Send text to Watson NLP and return the raw response text."""
    payload = {'raw_document': {'text': text_to_analyse}}
    response = requests.post(url=URL, headers=HEADERS, json=payload)
    return response.text
