from flask import Flask, request, redirect, render_template
import random
import string

app = Flask(__name__)

short_to_long_map = {}
long_to_short_map = {}
BASE_URL = "http://localhost:5000/"


def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shorten", methods=["POST"])
def shorten_url():
    long_url = request.json.get("long_url", "")
    if not long_url:
        return {"error": "Long URL not provided"}, 400

    if long_url in long_to_short_map:
        short_url = long_to_short_map[long_url]
    else:
        short_url = generate_short_url()
        short_to_long_map[short_url] = long_url
        long_to_short_map[long_url] = short_url

    return {"short_url": BASE_URL + short_url}


@app.route("/<short_url>", methods=["GET"])
def expand_url(short_url):
    long_url = short_to_long_map.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return {"error": "Short URL not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)
