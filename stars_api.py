from flask import Flask, jsonify, request
import pandas as pd
from data import data

df = pd.read_csv("C:/Users/arnav/Documents/coding/projects/Project_136/star_with_gravity.csv")
df.drop(["Unnamed: 0"], axis=1, inplace=True)

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

@app.route("/star")
def star():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": star_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()