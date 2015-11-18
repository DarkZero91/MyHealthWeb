from persistence.mysql import MySql

class PulseDao(object):
	dao = None
	table = "pulse"

	@classmethod
	def get_instance(cls):
		if not (cls.dao):
			cls.dao = cls()
		return cls.dao

	def __init__(self):
		self.db = MySql.get_instance()

	def save(self, pulse):
		sql = "INSERT INTO %s (id, heartrate, created) VALUES (%d, %d, \"%s\")" % (
			self.table, pulse.get_id(), pulse.get_heartrate(), pulse.get_timestamp())
		self.db.query(sql)
		
