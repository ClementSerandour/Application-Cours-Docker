from flask import Flask, render_template, request
import requests, os

app = Flask(__name__)
BACKEND_URL = "http://backend:9000"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    try:
        r = requests.get(f"{BACKEND_URL}/test")
        data = r.json()
        return render_template("test.html", data=data),200
    except Exception as e:
        return render_template('503.html'),503

@app.route("/db")
def db():
    try:
        r = requests.get(f"{BACKEND_URL}/db")
        data = r.json()
        return render_template("db.html", data=data)
    except Exception as e:
        return render_template('503.html')

@app.route("/vars")
def args():
    version = os.getenv("version")
    return render_template("args.html", data={"Version de python": version})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001, debug=True)
