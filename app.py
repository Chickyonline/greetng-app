from flask import Flask, render_template, request
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    greeting = None

    if request.method == "POST":

        name = request.form.get("name", "").strip()

        if name:

            # Use Dubai time
            current_time = datetime.now(ZoneInfo("Asia/Dubai"))
            hour = current_time.hour

            if hour < 12:
                greeting = f"Good morning, {name}!"
            elif hour < 18:
                greeting = f"Good afternoon, {name}!"
            else:
                greeting = f"Good evening, {name}!"

    return render_template(
        "index.html",
        greeting=greeting
    )


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)