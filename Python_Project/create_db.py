import sqlite3  #database

def create_db():
    con=sqlite3.connect(database='ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT ,name text, email text, gender text, contact text, dob text, doj text ,pass text, utype text, address text, salary text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT ,name text, contacttext, desc text)")
    con.commit()
    
    
create_db()    