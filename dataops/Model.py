# Product Service
from flask import Flask, request, jsonify, render_template, url_for
from flask_restful import Resource, Api
import _pickle as pickle
import numpy as np
from sklearn import datasets, linear_model
# import numpy as np
# from sklearn import datasets, linear_model

app = Flask(__name__)
api = Api(app)

knn_model = './knn.pkl'
logreg_model = './logreg.pkl'

iris_target_names = ['setosa', 'versicolor', 'virginica']

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
    Prediction = iris_target_names[Answer.item()]
    # return jsonify(iris_target_names[Answer.item()])
    return render_template('result.html', prediction=Prediction)

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
    Prediction = iris_target_names[Answer.item()]
    # return jsonify(iris_target_names[Answer.item()])
    return render_template('result.html', prediction=Prediction)

@app.route('/')
def index():
    # return "Please run /knn or /logreg with sl, sw, pl, pw as parameters"
    return render_template('index.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5071, debug=True)