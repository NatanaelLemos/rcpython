from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def post():
    print(getDirection())
    return "<p>Hello, World!</p>"


def getDirection():
    content = request.json
    return int(content["direction"])
