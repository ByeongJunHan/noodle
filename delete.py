import sqlite3
def ramen_delete(name_input):
    conn=sqlite3.connect("ramen.sqlite",isolation_level=None)
    c = conn.cursor()
    c.execute("DELETE FROM table1 WHERE name=?", (name_input,)) 
    conn.commit()

