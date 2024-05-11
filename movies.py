class Movie:
	def __init__(self,id,name,release_date, timestamps):
		self.id = id
		self.name = name
		self.release_date = release_date
		self.timestamps = timestamps
	def __repr__(self):
		return f"Id :{self.id}, Name : {self.name}"

	def data(self):
		return {
			"id":self.id,
			"name":self.name,
			"release_date":self.release_date,
			"timestamp":self.timestamp
		}	
        
