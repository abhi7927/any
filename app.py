from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)
 
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/more", methods = ["POST"])
def more():
	name=int(request.form.get("name"))
	name_num=randint(1,name)
	return render_template("more.html",name=name_num)