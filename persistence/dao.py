from persistence.mysql import MySql

class Dao(object):
	dao = None
	table = None

	@classmethod
	def get_instance(cls):
		if not (cls.dao):
			cls.dao = cls()
		return cls.dao

	def __init__(self):
		self.db = MySql.get_instance()

	def save(self, model):
		print "Not implemented!"

	def get(self, id):
		print "Not implemented!"

	def delete(self, id):
		print "Not implemented!"

	def list(self):
		print "Not implemented!"
		
