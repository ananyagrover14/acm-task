from flask import Flask, render_template, request, send_from_directory
import requests
import pymongo

app = Flask(__name__)

MONGO_DB = None 
def connectToDatabase():
	global MONGO_DB
	client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.3fqn2.mongodb.net/?retryWrites=true&w=majority")
	MONGO_DB = client["acm-task"]

@app.route('/')
def index():
	users = list(MONGO_DB.users.find())
	return render_template("index.html", users = users)

@app.route('/admin')
def getForm():
	
	return render_template("form.html")

@app.route('/delete')
def delete():
	query = { "Email": request.args.get("email") }
	MONGO_DB.users.delete_one(query)
	return index()

@app.route('/insert', methods=['POST'])
def insert():
	name = request.form['name']
	email =  request.form['email']
	acc_bal =  request.form['acc_bal']
	d = {"Name": name , "Account Balance": acc_bal , "Email": email}
	MONGO_DB.users.insert_one(d)
	return render_template("form.html", message = "Added Successfully")

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
   connectToDatabase() 
   app.run(debug = True)  