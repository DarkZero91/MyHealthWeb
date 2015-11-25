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
		self.db.con.commit()

	def delete(self, id):
		sql = "DELETE FROM %s WHERE id = %d;" %(self.table, id)
		self.db.query(sql)
		self.db.con.commit()
	
	def list(self):
		sql = "SELECT * FROM %s;" % self.table
		result = self.db.query(sql)
		return result.fetchall()
