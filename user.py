class User:
	def __init__(self,id,name,password,timestamp):
		self.id = id
		self.name = name
		self.__password = password
		self.timestamp = timestamp

	def data(self):
		return {
		"id":self.id,
		
		}