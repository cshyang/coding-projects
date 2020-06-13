import psycopg2
import pandas as pd


def create_table():
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres123' host='localhost' port='5432' " )  # step1: create a connection to the database
    cur = conn.cursor()  # step2: create a cursor object
    # write sql code
    cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")  # execute sql code
    conn.commit()
    conn.close()


def insert_value(item, quantity, price):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres123' host='localhost' port='5431' " )
    cur = conn.cursor()
    cur.execute( "INSERT INTO store VALUES (?,?,?)", (item, quantity, price))  # execute sql code
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres123' host='localhost' port='5431' " )
    cur = conn.cursor()
    cur.execute( "SELECT * FROM store" )
    data = cur.fetchall()
    conn.close()
    return pd.DataFrame(data)

def delete(item):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute( "DELETE FROM store WHERE item = ?", (item,) )
    conn.commit()
    conn.close()


def update(item, quantity, price):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute( "UPDATE FROM store SET quantity=?, price=? WHERE item = ?", (quantity,price,item) )
    conn.commit()
    conn.close()

create_table()

