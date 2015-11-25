import json
from models.pulse import Pulse
from models.ecg import ECG
from models.bloodpressure import BloodPressure
from persistence.pulsedao import PulseDao
from persistence.ecgdao import ECGDao
from persistence.bloodpressuredao import BloodPressureDao

class MyHealth(object):
	# PULSE
	def pulse_add(self, pulse_json):
		data = json.loads(pulse_json)

		pulse = Pulse(
			data["id"],
			data["heartrate"],
			data["created"])
		
		dao = PulseDao.get_instance()
		dao.save(pulse)

	def pulse_delete(self, id):
		dao = PulseDao.get_instance()
		dao.delete(id)

	def pulse_list(self):
		dao = PulseDao.get_instance()
		return json.dumps(dao.list())

	# ECG
	def ecg_add(self, ecg_json):
		data = json.loads(ecg_json)
		
		ecg = ECG(
			data["id"],
			data["data"],
			data["created"])

		dao = ECGDao.get_instance()
		dao.save(ecg)

	def ecg_get(self, id):
		dao = ECGDao.get_instance()
		return json.dumps(dao.get(id))

	def ecg_delete(self, id):
		dao = ECGDao.get_instance()
		dao.delete(id)

	def ecg_list(self):
		dao = ECGDao.get_instance()
		return json.dumps(dao.list())

	# BLOOD PRESSURE
	def bloodpressure_add(self, bloodpressure_json):
		data = json.loads(bloodpressure_json)
		
		bloodpressure = BloodPressure(
			data["id"],
			data["over"],
			data["under"],
			data["created"])

		dao = BloodPressureDao.get_instance()
		dao.save(bloodpressure)

	def bloodpressure_delete(self, id):
		dao = BloodPressureDao.get_instance()
		dao.delete(id)

	def bloodpressure_list(self):
		dao = BloodPressureDao.get_instance()
		return json.dumps(dao.list())
