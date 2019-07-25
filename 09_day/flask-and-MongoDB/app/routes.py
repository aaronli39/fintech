import os
from app import app
from flask import render_template, request, redirect

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"},
        {"event":"Fintech Graduation", "date":"2019-08-03"},
        {"event":"Date", "date":"2019-07-26"},
        {"event":"Fintech Trip", "date":"2019-07-25"}
    ]

password = "duMJ42KGtQfTFEKh"

# from flask_pymongo import PyMongo
from flask_pymongo import PyMongo

# name of database
app.config["test"] = 'test' 

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://aaronli39:duMJ42KGtQfTFEKh@fintech-v2rh1.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    eventsDB = mongo.db.events

    # make a query
    # empty curly braces will return all dictionaries
    events = eventsDB.find({"date": "2019-10-31"})
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    users = mongo.db.users

    # insert new data
    users.insert({
        "name": "sophia"
    })

    print("user created")
    # return a message to the user
    return render_template("index.html", events=events)

@app.route("/addEvent")
def addEvent():
    events = mongo.db.events

    events.insert({"event": "Halloween", "date": "2019-10-31"})

    print("Event added")
    return redirect("/")