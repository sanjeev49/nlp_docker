from distutils.log import debug
import json
from unittest import result
from flask import Flask, jsonify, request 

from utilities import predict_pipeline

app = Flask(__name__)

@app.post('/predict')
def predict():
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error':'No text was sent'})
    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        result =  jsonify({'error', str(e)})
    return result

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)

# to check the api 
# curl -X POST -H "Content-Type: application/json" -d '{"text":"May the Force be with you."}' 0.0.0.0:5000/predict
# write this command . 