from flask import Flask
from flask import render_template, redirect, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ajax", methods=["GET"])
def response():
    if request.values["type"] == "1":
        return jsonify(str(len(request.values["word"])))
    elif request.values["type"] == "2":
        return jsonify(request.values["word"][::-1])


if __name__ == "__main__":
    app.debug = True
    app.run()
