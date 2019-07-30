import os
from app import app
from flask import render_template, request, redirect, jsonify
from flask_pymongo import PyMongo

# name of database
app.config["music"] = "prefs"

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://aaronli39:duMJ42KGtQfTFEKh@fintech-v2rh1.mongodb.net/music?retryWrites=true&w=majority"

mongo = PyMongo(app)


# INDEX

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

@app.route('/add')

def add():
    # define a variable for the collection you want to connect to
    handle = mongo.db.music
    # use some method on that variable to add/find/delete data

    # return a message to the user (or pass data to a template)
    return ''


# SHOW A LIST OF ALL SONG TITLES




# ADVANCED: A FORM TO COLLECT USER-SUBMITTED SONGS




# DOUBLE-ADVANCED: SHOW ARTIST PAGE




# TRIPLE-ADVANCED: SHOW SONG PAGE


