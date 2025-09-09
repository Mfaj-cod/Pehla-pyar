from flask import Flask, render_template, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "829033f7-7836-4d77-80a9-c4c7f4299704"
URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

def fetch_crypto():
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY,
    }
    params = {"start": "1", "limit": "10", "convert": "USD"}

    try:
        response = requests.get(URL, headers=headers, params=params)
        return response.json()["data"]
    except Exception as e:
        print("Error fetching data:", e)
        return []

@app.route("/")
def index():
    cryptos = fetch_crypto()
    return render_template("index.html", cryptos=cryptos)

@app.route("/api/cryptos")
def api_cryptos():
    cryptos = fetch_crypto()
    return jsonify(cryptos)


@app.route("/about")
def about():
    return render_template("about.html")

@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

if __name__ == "__main__":
    app.run(debug=True)
