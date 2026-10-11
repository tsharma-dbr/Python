"""Flask web server for the Emotion Detection application."""

from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Render the application form."""
    return render_template("index.html", result=None, error=None, input_text="")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """Validate user input and display the detected emotions."""
    text_to_analyze = request.values.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        message = "Invalid input! Please enter some text to analyze."
        return render_template(
            "index.html", result=None, error=message, input_text=text_to_analyze
        ), 400

    result = emotion_detector(text_to_analyze)
    if result is None:
        message = "The emotion analysis service is unavailable. Please try again."
        return render_template(
            "index.html", result=None, error=message, input_text=text_to_analyze
        ), 502

    if result.get("dominant_emotion") is None:
        message = "Invalid input! Please enter valid text to analyze."
        return render_template(
            "index.html", result=None, error=message, input_text=text_to_analyze
        ), 400

    return render_template(
        "index.html", result=result, error=None, input_text=text_to_analyze
    )


if __name__ == "__main__":
    # Debug mode is disabled so the development debugger is not exposed.
    app.run(host="127.0.0.1", port=5000, debug=False)
