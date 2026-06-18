"""
Flask server for the Emotion Detection application.
Provides web routes to analyze text and return emotion scores.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/sentimentAnalyzer")
def emo_detector():
    """Analyze the given text and return the emotion scores and dominant emotion."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    return f"For the given statement, the system response is 'anger': {anger}, \
'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
The dominant emotion is {dominant_emotion}."


@app.route("/")
def render_index_page():
    """Render the main index page of the application."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    