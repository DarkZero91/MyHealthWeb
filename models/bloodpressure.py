class BloodPressure(object):
	def __init__(self, id, over, under, timestamp):
		self.id = id
		self.over = over
		self.under = under
		self.timestamp = timestamp

	def get_id(self):
		return self.id

	def get_over(self):
		return self.over
	
	def get_under(self):
		return self.under

	def get_timestamp(self):
		return self.timestamp
