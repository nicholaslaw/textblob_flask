from flask_restful import Resource, Api
from textblob import TextBlob
from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)
api = Api(app)

@app.route('/',methods=['POST'])
def predict():

    result = {"text": "", "sentiment": None}
    data = request.get_json()
    text = data.get("text")
    if text:
        result["text"] = text
        result["sentiment"] = TextBlob(text).sentiment.polarity

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')