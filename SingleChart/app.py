from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template

app = Flask(__name__)
 
@app.route("/barchart")
def bar_chart():
	labels = ["January","February","March","April","May","June","July","August"]
	values = [10,9,8,7,6,4,7,8]
	return render_template('barchart.html', values=values, labels=labels)

@app.route("/linechart")
def line_chart():
	labels = ["January","February","March","April","May","June","July","August"]
	values = [10,9,8,7,6,4,7,8]
	return render_template('linechart.html', values=values, labels=labels)

@app.route("/piechart")
def pie_chart():
	labels = ["January","February","March","April","May","June","July","August"]
	values = [10,9,8,7,6,4,7,8]
	colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
	return render_template('piechart.html', set=zip(values, labels, colors))

@app.route("/home")
def home_page():
	return render_template('homepage.html')
 
if __name__ == "__main__":
	app.run(host='localhost', port=5001)
