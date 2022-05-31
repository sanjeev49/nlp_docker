from crypt import methods
from distutils.log import debug
import json
# from matplotlib import projections
# from more_itertools import sample

from numpy import require
from flask import Flask , request, jsonify, render_template
from utilities import predict_pipeline

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('predict.html')


@app.route("/predict", methods=['POST'])
#@cross_origin()
def predictRoute():
    data = request.json['data']
    data = data.split(".")
    print(data)
    result = predict_pipeline(data)
    return jsonify({ "text" : result})
    

# @app.route('/predict', methods = ['GET','POST'])
# def predict():
#     if request.method == 'POST':
#         try:
#             sample  = request.form.get('fname')
#         except:
#             jsonify({"error", str(e)})
#         try:
#             if type(sample) == str:
#                 text = sample
#         except:
#             jsonify({'error', str(e)})
#     sample = [text]
#     predictions = predict_pipeline(sample)
#     return jsonify(predictions)

if __name__ == '__main__':
    app.run(port = 7000, host = '0.0.0.0', debug = True)
