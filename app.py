from flask import Flask, render_template, request, redirect, url_for, json
import requests
import credentials


app = Flask(__name__)

# app name
@app.errorhandler(404)
  
# inbuilt function which takes error as parameter
def not_found(e):
  
# defining function
  return render_template("404.html")

@app.route("/")
def index():
    api_key = credentials.API_KEY
    req = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + api_key)
    data = json.loads(req.content)
    return render_template('index.html', data=data)


@app.route("/image-archive", methods=['GET', 'POST'])
def archive():
    if request.method == "POST":
        start_date = request.form.get('start')
        end_date = request.form.get('end')
        api_key = credentials.API_KEY
        req = requests.get("https://api.nasa.gov/planetary/apod?api_key=" +
                           api_key + "&start_date=" + start_date +
                           "&end_date=" + end_date)
        data = json.loads(req.content)
        return render_template('archive.html', data=data)

    api_key = credentials.API_KEY
    req = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + api_key)
    data = json.loads(req.content)
    return render_template('archive.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)