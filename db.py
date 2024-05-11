import sqlite3, random, datatime
from movies import Movie

def get_random():
				random.getrandbit(28)

movie = [
{
"name":"The Three Body Problem",
"id":get_random(),
"release_date":datatime.datatime.now(),
"timestamps":datatime.datatime.now()
},
{
"name":"Friends",
"id":get_random(),
"release_date":datatime.datatime.now(),
"timestamps":datatime.datatime.now()
},
{
"name":"Modern Family",
"id":get_random(),
"release_date":datatime.datatime.now(),
"timestamps":datatime.datatime.now()
},
{
"name":"The Devil",
"id":get_random(),
"release_date":datatime.datatime.now(),
"timestamps":datatime.datatime.now()
},
{
"name":"Interstellar",
"id":get_random(),
"release_date":datatime.datatime.now(),
"timestamps":datatime.datatime.now()
},
{
"name":"Actionale",
"id":get_random(),
"release_date":datatime.datatime.now(),
"timestamps":datatime.datatime.now()
},
{
"name":"anabelle",
"id":get_random(),
"release_date":datatime.datatime.now(),
"timestamps":datatime.datatime.now()
},
{
"name":"Conjuring",
"id":get_random(),
"release_date":datatime.datatime.now(),
"timestamps":datatime.datatime.now()
},
{
"name":"Get Together",
"id":get_random(),
"release_date":datatime.datatime.now(),
"timestamps":datatime.datatime.now()
},
{
"name":"Making the Mistake",
"id":get_random(),
"release_date":datatime.datatime.now(),
"timestamps":datatime.datatime.now()
},
]

def connect():
	conn = sqlite3.connect("movies.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXIST movies(id INTEGER PRIMARY KEY,name TEXT, release_date TEXT, timestamp TEXT)")
	conn.commit()
	conn.close()
        for i in movies:
    	mv = Movie(i["id"],i["name"],i["release_date"],i["timestamps"])
    	insert(mv)


def insert(movie):
	conn = sqlite3.connect("movies.db")
	cur= conn.cursor()
	cur.execute("INSERT INTO movies(?,?,?,?)",(
		movie.id,
		movie.name,
		movie.release_date,
        movie.timestamps
		)
        conn.commit()
        conn.close()

def get():
        conn = sqlite3.connect("movies.db")
	       cur= conn.cursor()
	cur.execute("SELECT * FROM movies")
	rows = cur.fetchall()
	arr = []
	for i in rows:
		mv = Movie(i[0],i[1],i[2],i[3])
		arr.append(mv)
        conn.commit()
        conn.close()
        return arr

def update(movie):    
        conn = sqlite3.connect("movies.db")
	cur= conn.cursor()
	cur.execute("UPDATE movies SET name = ?, release_date = ? , timestamp = ? WHERE id = ?",(
		movie.name,
		movie.release_date,
                movie.timestamps,
                movie.id
		))
        conn.commit()
        conn.close()

def delete(movie):
        conn = sqlite3.connect("movies.db")
	cur= conn.cursor()
	cur.execute("DELETE FROM movies WHERE id = ?",(movie.id))
        conn.commit()
        conn.close()
