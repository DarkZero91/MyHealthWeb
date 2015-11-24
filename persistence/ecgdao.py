from persistence.dao import Dao

class ECGDao(Dao):
	table = "ecg"

	def __init__(self):
		super(ECGDao, self).__init__()

	def save(self, ecg):
		data = ",".join(map(str, ecg.get_data()))
		sql = "INSERT INTO %s (id, data, created) VALUES (%d, \"%s\", \"%s\")" % (
			self.table, ecg.get_id(), data, ecg.get_timestamp())
		self.db.query(sql)
		self.db.con.commit()
		
