import _mysql
import sys

class MySql(object):
	db = None
	host = "localhost"
	user = "myhealth"
	password = "test123"
	database = "myhealth"

	@classmethod
	def get_instance(cls):
		if not (cls.db):
			cls.db = cls()
		return cls.db

	def __init__(self):
		self.connect()

	def connect(self):
		try:
			self.con = _mysql.connect(self.host, self.user, self.password, self.database)
		except _mysql.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	def disconnect(self):
		self.con.close()

	def query(self, query):
		self.con.query(query)
		return self.con.use_result()
