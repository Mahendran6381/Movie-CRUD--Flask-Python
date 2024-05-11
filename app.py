from flask import *
from movies import Movie
import db
app = Flask(__name__)

if not os.path.isfile('movies.db'):
	db.connect()
	arr = db.get()
	for i in arr:
		print(i.name)

@app.route("/")
def home():
   return "hello World"
	


if __name__  == "__main__":
	app.run()