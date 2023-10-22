'''
This is a flask server
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("EmotionDetection", template_folder="templates")

@app.route("/emotion_predictor")
def emotion_predictor_function():
    '''
    This function calls the application
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_predictor(text_to_analyze)

    if response[0]['dominant_emotion'] is None:
        response_text = "Invalid Input!"
    else:
        response_text = ("For the given statement, the system response is 'anger': "
                         f"{response[0]['anger']}, 'disgust': {response[0]['disgust']}, "
                         f"'fear': {response[0]['fear']}, 'joy': {response[0]['joy']}, "
                         f"'sadness': {response[0]['sadness']}. The dominant emotion is "
                         f"{response[0]['dominant_emotion']}.")

    return response_text

@app.route("/")
def render_index_page():
    '''
    This is a function to render the index.html
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
