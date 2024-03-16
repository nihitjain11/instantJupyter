# Product Service
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import _pickle as pickle
# import numpy as np
# from sklearn import datasets, linear_model

app = Flask(__name__)
api = Api(app)

knn_model = './knn.pkl'
logreg_model = './logreg.pkl'

@app.route('/knn')
def knn():  
    sl = float(request.args.get('sl'))
    sw = float(request.args.get('sw'))
    pl = float(request.args.get('pl'))
    pw = float(request.args.get('pw'))
    data = [[sl, sw, pl, pw]]
    with open(knn_model, 'rb') as k:
        PickleModel = pickle.load(k)
    Answer = PickleModel.predict(data)
    return jsonify(Answer.tolist())

@app.route('/logreg')
def logreg():  
    sl = float(request.args.get('sl'))
    sw = float(request.args.get('sw'))
    pl = float(request.args.get('pl'))
    pw = float(request.args.get('pw'))
    data = [[sl, sw, pl, pw]]
    with open(logreg_model, 'rb') as k:
        PickleModel = pickle.load(k)
    Answer = PickleModel.predict(data)
    return jsonify(Answer.tolist())

@app.route('/')
def index():
    return "Please run /knn or /logreg with sl, sw, pl, pw as parameters"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5071, debug=True)