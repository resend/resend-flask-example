import resend
import os
from flask import Flask, jsonify

resend.api_key = os.environ["RESEND_API_KEY"]

app = Flask(__name__)


@app.route("/")
def index():
    params = {
        "from": "onboarding@resend.dev",
        "to": "delivered@resend.dev",
        "subject": "hello world",
        "html": "<strong>it works!</strong>",
    }

    r = resend.Emails.send(params)
    return jsonify(r)


if __name__ == "__main__":
    app.run()
