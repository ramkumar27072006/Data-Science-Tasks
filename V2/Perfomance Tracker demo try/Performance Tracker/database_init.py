import sqlite3
c=sqlite3.connect("database.db").cursor()
c.execute("CREATE TABLE IF NOT EXISTS students (roll_number TEXT PRIMARY KEY, name TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS grades (roll_number TEXT, subject TEXT, grade INTEGER)")
c.connection.commit()
