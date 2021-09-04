from flask import Flask, render_template, redirect, url_for, json
import requests
import credentials

app = Flask(__name__)



@app.route("/")
def index():
    api_key = credentials.API_KEY
    req = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + api_key)
    data = json.loads(req.content)
    return render_template('index.html', data=data)


@app.route("/about")
def about():
    api_key = credentials.API_KEY
    req = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + api_key)
    data = json.loads(req.content)
    return render_template('about.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)