"""Deterministic unit tests for EmotionDetection (no live network required)."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


API_PATH = "EmotionDetection.emotion_detection.requests.post"


def mock_success(emotions):
    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        "emotionPredictions": [{"emotion": emotions}]
    }
    return response


class TestEmotionDetector(unittest.TestCase):
    @patch(API_PATH)
    def test_joy(self, mock_post):
        mock_post.return_value = mock_success({
            "anger": 0.01, "disgust": 0.02, "fear": 0.03,
            "joy": 0.91, "sadness": 0.03,
        })
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.91)

    @patch(API_PATH)
    def test_anger(self, mock_post):
        mock_post.return_value = mock_success({
            "anger": 0.85, "disgust": 0.03, "fear": 0.04,
            "joy": 0.02, "sadness": 0.06,
        })
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch(API_PATH)
    def test_disgust(self, mock_post):
        mock_post.return_value = mock_success({
            "anger": 0.02, "disgust": 0.87, "fear": 0.03,
            "joy": 0.01, "sadness": 0.07,
        })
        result = emotion_detector("I feel disgusted by this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch(API_PATH)
    def test_sadness(self, mock_post):
        mock_post.return_value = mock_success({
            "anger": 0.03, "disgust": 0.02, "fear": 0.04,
            "joy": 0.01, "sadness": 0.90,
        })
        result = emotion_detector("I feel very sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch(API_PATH)
    def test_fear(self, mock_post):
        mock_post.return_value = mock_success({
            "anger": 0.03, "disgust": 0.02, "fear": 0.89,
            "joy": 0.01, "sadness": 0.05,
        })
        result = emotion_detector("I am afraid this may happen")
        self.assertEqual(result["dominant_emotion"], "fear")

    @patch(API_PATH)
    def test_http_400_returns_expected_none_values(self, mock_post):
        response = Mock()
        response.status_code = 400
        mock_post.return_value = response
        result = emotion_detector("invalid test input")
        self.assertEqual(result, {
            "anger": None, "disgust": None, "fear": None,
            "joy": None, "sadness": None, "dominant_emotion": None,
        })

    @patch(API_PATH)
    def test_server_error_returns_none(self, mock_post):
        response = Mock()
        response.status_code = 500
        mock_post.return_value = response
        self.assertIsNone(emotion_detector("sample text"))

    def test_blank_input_returns_expected_none_values_without_request(self):
        with patch(API_PATH) as mock_post:
            result = emotion_detector("   ")
            mock_post.assert_not_called()
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
