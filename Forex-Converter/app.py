
from flask import Flask, request, render_template, jsonify, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
import pdb
 
app = Flask(__name__)

app.config['SECRET_KEY'] = "blahblahblah123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route("/")
def converter():
	""" """
	#k = 'ce6a43f817716933ae8667d9c9c030f8'
	#f = 'USD'
	#t = 'EUR'
	#a = 10
	#r = (f'http://api.exchangerate.host/convert?access_key={k}&from={f}&to={t}&amount={a}');

	return render_template("index.html")

@app.route("/convert", methods=["POST"])
def conversion():
	""" """
	k = 'ce6a43f817716933ae8667d9c9c030f8'
	f = request.form["convertFrom"]
	t = request.form["convertTo"]
	a = request.form["amount"]
	return redirect(f'http://api.exchangerate.host/convert?access_key={k}&from={f}&to={t}&amount={a}')

