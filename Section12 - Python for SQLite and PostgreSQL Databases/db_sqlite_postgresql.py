import sqlite3

def create_table():
    # Connect to/create database
    conn = sqlite3.connect("lite.db")
    # create curson object
    cur = conn.cursor()
    # create table
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # commit changes to db
    conn.commit()
    # close connection to db
    conn.close()

create_table()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # add data to table
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

insert("Water Glass", 10, 5.5)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

print(view())
