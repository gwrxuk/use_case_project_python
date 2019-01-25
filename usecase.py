import os
import sys
import csv
import sqlite3

def insertData(data):
    conn = sqlite3.connect('usecase.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, age TEXT, area TEXT)''')
    inserted = 0 
    for row in data:
        c.execute("INSERT INTO users(name,age,area) VALUES ('"+row[0]+"','"+row[1]+"','"+row[2]+"')")
        inserted = inserted + 1
        conn.commit()
    print( str(inserted) +" records inserted.")
    records = c.execute('SELECT count(*) FROM users')
    print("Total records are "+ str(c.fetchone()[0]))

if len(sys.argv) > 1:
    print(sys.argv[1]);
    with open(sys.argv[1],'r') as csvfile:
        result = csv.reader(csvfile)
        insertData(result)
else:
    print("Please provide a CSV file name.")
