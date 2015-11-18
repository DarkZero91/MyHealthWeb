from persistence.dao import Dao

class BloodPressureDao(Dao):
	table = "bloodpressure"

	def __init__(self):
		super(BloodPressureDao, self).__init__()

	def save(self, bloodpressure):
		sql = "INSERT INTO %s (id, over, under, created) VALUES (%d, %d, %d, \"%s\")" % (
			self.table, bloodpressure.get_id(), bloodpressure.get_over(),
			bloodpressure.get_under(), bloodpressure.get_timestamp())
		self.db.query(sql)
		
