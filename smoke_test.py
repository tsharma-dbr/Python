"""Offline smoke test for import and output formatting."""
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


def main():
    emotions = {
        "anger": 0.02,
        "disgust": 0.01,
        "fear": 0.04,
        "joy": 0.88,
        "sadness": 0.05,
    }
    response = Mock()
    response.status_code = 200
    response.json.return_value = {"emotionPredictions": [{"emotion": emotions}]}
    with patch("EmotionDetection.emotion_detection.requests.post", return_value=response):
        result = emotion_detector("I am glad this happened")
    assert result is not None
    assert result["dominant_emotion"] == "joy"
    assert set(result) == {
        "anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"
    }
    print("Import test: PASS")
    print("Formatted-output smoke test with mocked HTTP response: PASS")
    print("Mock output:", result)
    print("Note: mock output only; not a live Watson API response.")


if __name__ == "__main__":
    main()
