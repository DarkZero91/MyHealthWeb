import json
from models.pulse import Pulse
from persistence.pulsedao import PulseDao

class MyHealth(object):
	def pulse_add(self, pulse_json):
		data = json.loads(pulse_json)

		pulse = Pulse(
			data["id"],
			data["heartrate"],
			data["timestamp"])
		
		dao = PulseDao.get_instance()
		dao.save(pulse)

		return True
