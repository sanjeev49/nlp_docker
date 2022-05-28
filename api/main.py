from distutils.log import debug

from numpy import require
from flask import Flask , request, jsonify, render_template
from utilities import predict_pipeline

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        try:
            sample  = request.form.get('fname')
        except:
            jsonify({"error", str(e)})

if __name__ == "__main__":
    app.run(debug= True)
