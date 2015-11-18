from flask import Flask
from flask import request
from myhealth import MyHealth

app = Flask(__name__)
service = MyHealth()

# Status Codes:
notfound = 404
invalid = 402
ok = 200


@app.route("/measurement/pulse", methods=["POST"])
def add_pulse_measurement():
	service.pulse_add(request.form["data"])
	return "pulse measurement added", ok

@app.route("/measurement/ecg", methods=["POST"])
def add_ecg_measurement():
	service.ecg_add(request.form["data"])
	return "ecg measurement added", ok


if __name__ == "__main__":
	app.run(host='0.0.0.0')
