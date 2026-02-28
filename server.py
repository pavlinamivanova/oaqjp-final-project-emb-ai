''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion sentiment analysis over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    res_return = ""
    if response["dominant_emotion"] is None:
        res_return = " Invalid text! Please try again! "
    else:
        res_return = f"For the given statement, the system response is {response}.\
        The dominant emotion is <b>{response['dominant_emotion']}</b>."
        #Return a formatted string with the sentiment label and score 
    return res_return

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
