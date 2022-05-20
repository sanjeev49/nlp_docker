from crypt import methods
from distutils.log import debug
import json
from unittest import result
from flask import Flask, jsonify, request , render_template

from utilities import predict_pipeline

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict')


def predict():
    if request.method == 'POST':
        data = request.form.get_items()
        print(data)
    else:
        print('not a post request')
        return render_template('index.html')


# @app.post('/predict')
# def predict():
#     data = request.json
#     try:
#         sample = data['text']
#     except KeyError:
#         return jsonify({'error':'No text was sent'})
#     sample = [sample]
#     predictions = predict_pipeline(sample)
#     try:
#         result = jsonify(predictions[0])
#     except TypeError as e:
#         result =  jsonify({'error', str(e)})
#     return result

# if __name__ == '__main__':
#     app.run(host = '0.0.0.0', debug = True)

if __name__ == '__main__':
    app.run(debug= True)

# to check the api 
# curl -X POST -H "Content-Type: application/json" -d '{"text":"You are most horrible person i have ever met"}' 0.0.0.0:5000/predict
# write this command . 
# def pred():
    
#     sample = ["hi what is your name", "where are you going", "he is such a bad person"]
#     predictions = predict_pipeline(sample)
#     print(predictions[0])
# pred()