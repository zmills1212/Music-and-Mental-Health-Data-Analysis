import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

flask_app = Flask(__name__)
mlp_classifier = pickle.load(open('model.pkl','rb'))


@flask_app.route("/")   
def index():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])   
def predict():
    f =[int(x) for x in request.form.values()]
    f = [np.array(f)]
    result = mlp_classifier.predict(f)
    return render_template("index.html", pred_result = result)

if __name__ =="__main__":
    flask_app.run(debug = True)


