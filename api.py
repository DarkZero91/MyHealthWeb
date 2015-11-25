from flask import Flask
from flask import request
from myhealth import MyHealth

app = Flask(__name__)
service = MyHealth()

# Status Codes:
notfound = 404
invalid = 402
ok = 200

# PULSE
@app.route("/measurement/pulse", methods=["POST"])
def add_pulse_measurement():
	service.pulse_add(request.data)
	return "pulse measurement added", ok

@app.route("/measurement/pulse/<id>", methods=["DELETE"])
def delete_pulse_measurement(id):
	service.pulse_delete(int(id))
	return "pulse measurement deleted", ok

@app.route("/measurement/pulses", methods=["GET"])
def list_pulse_measurement():
	return service.pulse_list(), ok

# ECG
@app.route("/measurement/ecg", methods=["POST"])
def add_ecg_measurement():
	service.ecg_add(request.data)
	return "ecg measurement added", ok

@app.route("/measurement/ecgs", methods=["GET"])
def list_ecg_measurements():
	return service.ecg_list(), ok

# BLOOD PRESSURE
@app.route("/measurement/bloodpressure", methods=["POST"])
def add_bloodpressure_measurement():
	service.bloodpressure_add(request.data)
	return "blood pressure measurement added", ok

@app.route("/measurement/bloodpressures", methods=["GET"])
def list_bloodpressure_measurements():
	return service.bloodpressure_list(), ok


if __name__ == "__main__":
	app.run(host='0.0.0.0')
