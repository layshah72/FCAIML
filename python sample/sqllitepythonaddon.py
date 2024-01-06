import sqlite3

conn = sqlite3.connect('myDatabase1.db')
cursore = conn.cursor()

#create a table
cursore.execute('''CREATE TABLE IF not Exists users
                    (id INTEGER PRIMARY KEY ,name TEXT, age INTEGER)''')

#Insert some data
cursore.execute("INSERT INTO users (name,age) VALUES (?,?)",("Alice",25))
cursore.execute("INSERT INTO users (name,age) VALUES (?,?)",("Bob",30))


conn.commit()

#Retrieve Data
cursore.execute("select * FROM users")
print(cursore.fetchall())
