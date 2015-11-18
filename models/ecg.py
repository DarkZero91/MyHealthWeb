class ECG(object):
	def __init__(self, id, data, timestamp):
		self.id = id
		self.data = data
		self.timestamp = timestamp

	def get_id(self):
		return self.id

	def get_data(self):
		return self.data

	def get_timestamp(self):
		return self.timestamp
