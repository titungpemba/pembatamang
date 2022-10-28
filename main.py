from django.shortcuts import render
from flask import Flask, render_template

app = Flask(__name__, template_folder="template", static_folder="static")

@app.route("/")
def hello_world():
    return render_template("index.html")

app.run(host="0.0.0.0", port = 8001, debug=True)