from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

# Adds a pulse measurement
@app.route("/measurement/pulse", methods=["POST"])
def add_pulse_measurement():
	return request.form["test"]

if __name__ == "__main__":
	app.run(host='0.0.0.0')
