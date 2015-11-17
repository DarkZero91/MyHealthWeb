from flask import Flask
from flask import request
from myhealth import MyHealth

app = Flask(__name__)
service = MyHealth()

# Status Codes:
notfound = 404
invalid = 402
ok = 200


### Adds a pulse measurement ###
@app.route("/measurement/pulse", methods=["POST"])
def add_pulse_measurement():
	if service.pulse_add(request.form["data"]):
		return "pulse measurement added", ok
	else:
		return "unable to add pulse measurement", invalid

if __name__ == "__main__":
	app.run(host='0.0.0.0')
