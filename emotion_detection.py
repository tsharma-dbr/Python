"""Compatibility entry point used during Task 2 before packaging.

The final implementation lives in the EmotionDetection package. Keeping this
module allows the required Task 2 import style:
    from emotion_detection import emotion_detector
"""
from EmotionDetection.emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
