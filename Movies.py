import sqlite3

conn=sqlite3.connect("Moviedb.sqlite")
cur=conn.cursor()
cur.execute('''Drop table  if exists Movies''')
cur.execute('''CREATE TABLE Movies (Name text,Actor text,Director text,Year int)''')
cur.execute('''Insert into Movies(Name,Actor,Director,Year)values("Interstellar","Matthew McConaughey","Christopher Nolan",2014)''')
cur.execute('''Insert into Movies(Name,Actor,Director,Year)values("Gravity","George Clooney","Alfonso Cuarón",2013)''')
cur.execute('''Insert into Movies(Name,Actor,Director,Year)values("Furious 7","Vin Diesel","James Wan",2015)''')
cur.execute('''Insert into Movies(Name,Actor,Director,Year)values("Fast Five","Vin Diesel","Justin Lin",2011)''')
conn.commit()

sql=['SELECT *from Movies',"Select * from Movies where Actor= 'Vin Diesel' "]

for query in sql:
    for movie in cur.execute(query):
        print(movie[0],movie[1],movie[2],movie[3])
    print("\n\n")    


