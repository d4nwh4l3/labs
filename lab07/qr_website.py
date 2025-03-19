from flask import Flask, render_template, request
import segno

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code = None
    message = None

    if request.method == "POST":
        message = request.form["data"]
        qr = segno.make(message)
        qr_code = qr.svg_data_uri(scale=4)

    return render_template("index.html", qr_code=qr_code, message=message)

if __name__ == "__main__":
    app.run(debug=True)