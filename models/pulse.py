class Pulse(object):
	def __init__(self, id, heartrate, timestamp):
		self.id = id
		self.heartrate = heartrate
		self.timestamp = timestamp
	
	def get_id(self):
		return self.id
	
	def get_heartrate(self):
		return self.heartrate

	def get_timestamp(self):
		return self.timestamp
