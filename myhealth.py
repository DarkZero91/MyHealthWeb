import json
from models.pulse import Pulse
from models.ecg import ECG
from persistence.pulsedao import PulseDao
from persistence.ecgdao import ECGDao

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
