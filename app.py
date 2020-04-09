
import nexmo
from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('.env')


@app.route('/')
def index():
    return "Success! Endpoints available: /request /check and /cancel."


@app.route('/request/<to_number>/<brand>')
def request(to_number, brand):
    client = nexmo.Client(app.config.get('NEXMO_API_KEY'), app.config.get('NEXMO_API_SECRET'))
    response = client.start_verification(
        number=to_number,
        brand=brand,
        code_length="6")

    if response["status"] == "0":
        return "Request_id is: " + response["request_id"]
    else:
        return "Error: " + response["error_text"]


@app.route('/check/<request_id>/<code>')
def check(request_id, code):
    client = nexmo.Client(app.config.get('NEXMO_API_KEY'), app.config.get('NEXMO_API_SECRET'))
    response = client.check_verification(request_id, code=code)

    if response["status"] == "0":
        return "Verification successful, event_id is: " + response["event_id"]
    else:
        return "Error: " + response["error_text"]


@app.route('/cancel/<request_id>')
def cancel(request_id):
    client = nexmo.Client(app.config.get('NEXMO_API_KEY'), app.config.get('NEXMO_API_SECRET'))
    response = client.cancel_verification(request_id)

    if response["status"] == "0":
        return "Cancellation successful."
    else:
        return "Error: " + response["error_text"]
