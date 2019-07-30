import os
from app import app
from flask import render_template, request, redirect, jsonify

from flask_pymongo import PyMongo

# name of database
app.config["test"] = "test"

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://aaronli39:duMJ42KGtQfTFEKh@fintech-v2rh1.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)


# INDEX

@app.route('/', methods=["POST", "GET"])
def index():
    events = []
    event = mongo.db.events.find({})
    for i in event:
        events.append(i)
    return render_template("index.html", events=events)

# This route will handle the POST of our form. It should also be able to redirect to homepage on a GET request
@app.route('/addevent', methods=["GET", "POST"])
def add_event():
    if request.method == "GET":
        return render_template('add_event.html')
    else:
        collection = mongo.db.events
        name = request.form["eName"]
        date = request.form["eDate"]
        print(name, date)
        collection.insert({"event": name, "date": date})
        return redirect("/")
