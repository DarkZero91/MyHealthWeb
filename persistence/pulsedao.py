from persistence.mysql import MySql
from persistence.dao import Dao

class PulseDao(Dao):
	table = "pulse"

	def __init__(self):
		super(PulseDao, self).__init__()

	def save(self, pulse):
		sql = "INSERT INTO %s (id, heartrate, created) VALUES (%d, %d, \"%s\")" % (
			self.table, pulse.get_id(), pulse.get_heartrate(), pulse.get_timestamp())
		self.db.query(sql)
		
