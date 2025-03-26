from flask import Flask, render_template, request
from apod_fetcher import fetch_apod

app = Flask(__name__)

@app.route("/")
def home():
    try:
        apod_data = fetch_apod()
        return render_template("index.html", apod=apod_data)
    except Exception as e:
        return f"Error fetching APOD: {e}"

@app.route("/history", methods=["GET", "POST"])
def history():
    apod_data = None
    if request.method == "POST":
        date = request.form.get("date")
        try:
            apod_data = fetch_apod(date)
        except Exception as e:
            return f"Error fetching APOD: {e}"
    return render_template("history.html", apod=apod_data)

if __name__ == "__main__":
    app.run(debug=True)