from flask import Flask, render_template, send_from_directory
import requests

app = Flask(__name__)


@app.route('/')
def index():
	response = requests.get("https://jsonplaceholder.typicode.com/todos")
	users= response.json()
	return render_template("index.html", users = users)


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
	app.run(debug = True)  