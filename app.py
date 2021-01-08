from flask_restful import Resource, Api
from textblob import TextBlob
from flask import Flask, render_template, request, url_for, jsonify
from elasticsearch import Elasticsearch
from datetime import datetime

app = Flask(__name__)
api = Api(app)

es = Elasticsearch("es01")

@app.route('/',methods=['POST'])
def predict():

    result = {"sentiment": None, "subjectivity": None, "created": False}
    data = request.get_json()
    
    text = data.get("text", "")
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    index_bool = es.index(index="sentiment",
                doc_type="test-type",
                body={"author": data.get("author", ""),
                    "timestamp": data.get("timestamp", datetime.now()),
                    "text": text,
                    "polarity": polarity,
                    "subjectivity": subjectivity
                    })

    result["sentiment"] = polarity
    result["subjectivity"] = subjectivity
    result["created"] = index_bool['result']

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')