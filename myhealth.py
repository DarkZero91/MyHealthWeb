import json
from models.pulse import Pulse
from models.ecg import ECG
from models.bloodpressure import BloodPressure
from persistence.pulsedao import PulseDao
from persistence.ecgdao import ECGDao
from persistence.bloodpressuredao import BloodPressureDao

class MyHealth(object):
	def pulse_add(self, pulse_json):
		data = json.loads(pulse_json)

		pulse = Pulse(
			data["id"],
			data["heartrate"],
			data["timestamp"])
		
		dao = PulseDao.get_instance()
		dao.save(pulse)

	def ecg_add(self, ecg_json):
		data = json.loads(ecg_json)
		
		ecg = ECG(
			data["id"],
			data["data"],
			data["timestamp"])

		dao = ECGDao.get_instance()
		dao.save(ecg)

	def bloodpressure_add(self, bloodpressure_json):
		data = json.loads(bloodpressure_json)
		
		bloodpressure = BloodPressure(
			data["id"],
			data["over"],
			data["under"],
			data["timestamp"])

		dao = BloodPressureDao.get_instance()
		dao.save(bloodpressure)
