"""Minimal setuptools configuration for the EmotionDetection package."""

from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    description="IBM Watson NLP emotion detection application",
    packages=find_packages(),
    install_requires=["requests>=2.31.0"],
)
