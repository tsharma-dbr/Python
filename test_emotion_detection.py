"""Five course-required live tests against the IBM Watson NLP endpoint."""
import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check the expected dominant emotion for the five course statements."""

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main(verbosity=2)
