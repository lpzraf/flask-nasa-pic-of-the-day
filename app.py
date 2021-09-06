from os import environ
from flask import Flask, render_template, request, json
import requests
import credentials


app = Flask(__name__)


# 404 page
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


# home page
@app.route("/")
def index():
    # api_key = credentials.API_KEY
    api_key = environ.get('API_KEY')
    req = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + api_key)
    data = json.loads(req.content)
    return render_template('index.html', data=data)


# img archive page
@app.route("/image-archive", methods=['GET', 'POST'])
def archive():
    if request.method == "POST":
        start_date = request.form.get('start')
        end_date = request.form.get('end')
        api_key = environ.get('API_KEY')
        req = requests.get("https://api.nasa.gov/planetary/apod?api_key=" +
                           api_key + "&start_date=" + start_date +
                           "&end_date=" + end_date)
        data = json.loads(req.content)
        return render_template('archive.html', data=data)

    api_key = environ.get('API_KEY')
    req = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + api_key)
    data = json.loads(req.content)
    return render_template('archive.html', data=data)


if __name__ == "__main__":
    app.run()