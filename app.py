from flask import Flask, render_template, request
from random import randint
name_list=[]


app = Flask(__name__)
 
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/more", methods = ["POST","GET"])
def more():
	if request.method=="POST":
		name=int(request.form.get("name"))
		name_list.append(name)

	else:
		name=name_list[-1]
	name_num=randint(1,name)
	return render_template("more.html",name=name_num)
