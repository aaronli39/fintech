from flask import Flask
from flask import render_template, request, redirect, jsonify
from flask_pymongo import PyMongo

import os

app = Flask(__name__)

# name of database
app.config["music"] = "prefs"

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://aaronli39:duMJ42KGtQfTFEKh@fintech-v2rh1.mongodb.net/music?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("template.html")

# ADD SONGS
@app.route("/ajax", methods=["POST", "GET"])
def ajax():
    if request.method == "POST":
        print("\nreceived post req, executing code\n")
        handle = mongo.db.prefs
        print(request.form)
        name = request.form.get("sName")
        art = request.form.get("sArt")
        desc = request.form.get("sDesc")
        print(name, art, desc)
        handle.insert({"name": name, "artist": art, "description": desc})
        return jsonify(output=name)

# SHOW SONG LIST
# @app.route("/listSongs") 
# def listSongs(): 

if __name__ == "__main__":
    app.run(debug = True)