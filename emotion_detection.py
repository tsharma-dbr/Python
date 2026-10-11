"""Emotion detection client for the IBM Watson NLP EmotionPredict service."""

from typing import Any, Dict, Optional

import requests

API_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTION_NAMES = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result() -> Dict[str, Optional[float]]:
    """Return the expected response structure when the input is invalid."""
    result: Dict[str, Optional[float]] = {name: None for name in EMOTION_NAMES}
    result["dominant_emotion"] = None  # type: ignore[assignment]
    return result


def emotion_detector(text_to_analyze: str) -> Optional[Dict[str, Any]]:
    """Return five emotion scores and the name of the dominant emotion.

    An HTTP 400 response is represented by the expected dictionary containing
    None values. Other HTTP/service or response-format errors return None.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            API_URL, headers=headers, json=payload, timeout=30
        )
    except requests.RequestException:
        return None

    if response.status_code == 400:
        return _empty_result()
    if response.status_code != 200:
        return None

    try:
        response_data = response.json()
        emotions = response_data["emotionPredictions"][0]["emotion"]
        scores = {name: float(emotions[name]) for name in EMOTION_NAMES}
    except (KeyError, IndexError, TypeError, ValueError):
        return None

    scores["dominant_emotion"] = max(
        EMOTION_NAMES, key=lambda name: scores[name]
    )
    return scores
