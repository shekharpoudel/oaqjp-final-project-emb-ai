from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")
@app.route("/")
def get_home_page():
     return render_template('index.html') #load index page with template renderer

@app.route("/emotionDetector") #this is where the javascript is calling
def sent_analyzer():
    # Retrieve the text for emotion from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_dict = emotion_detector(text_to_analyze)
    if emotion_dict['dominant_emotion'] is None:
        html_output = '<b>Invalid text! Please try again!</br>'
    else:
        html_output = (
        f"For the given statement, the system response is "
        f"'anger': {emotion_dict['anger']}, "
        f"'disgust': {emotion_dict['disgust']}, "
        f"'fear': {emotion_dict['fear']}, "
        f"'joy':  {emotion_dict['joy']} and "
        f"'sadness': {emotion_dict['sadness']}. "
        f"The dominant emotion is <b>{emotion_dict['dominant_emotion']}</b>.")
    return html_output # Return a formatted string

app.run(port=5000, debug=True)