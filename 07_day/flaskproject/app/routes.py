from app import app
from flask import render_template, request, redirect
from app.models import model, formopener
from flask import render_template
from app.models import model

@app.route('/')
@app.route('/index')
def index():
    nick = {"name": "Aaron"}
    print(nick)
    return render_template("index.html", title="Homepage", 
                            nick=nick)
    
# app.route creates a route we can get to on our url
# the function decides what that route should lead to
@app.route("/secret")
def secret():
    return "<h1>I love rubber duckies</h1>"

@app.route("/render")
def render():
    return render_template("index.html")

@app.route("/yeetus")
def hm():
    name = request.args.get("nickname")
    print(name)
    return render_template("temp.html", name=name)

@app.route("/sendBreakfast", methods=["POST", "GET"])
def breakfast():
    stuff = request.form
    if request.method == "GET":
        return redirect("yeetus")
    temp = request.form["breakfast"]
    temp = model.shout(temp)
    return render_template("results.html", name=stuff["nickname"], food=temp)

@app.route("/ajax")
def response():
    return "hello"
