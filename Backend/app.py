from flask import Flask, request
from flask_cors import CORS,cross_origin


import Diseaseprediction.disease_prediction as m

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def home():
    args = request.args
    x = m.NaiveBayesWithProps(args["s1"],args["s2"],args["s3"],args["s4"],args["s5"])
    return {"disease" : x}

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)