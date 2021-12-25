import sqlite3
def ramen_add(name_input,num_input,type_input):
    conn = sqlite3.connect("ramen.sqlite", isolation_level=None)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS table1 \
        (name text, num interger, type text)")
    c.execute("SELECT num FROM table1 WHERE name=? AND type=?", {"Name": name_input,"Type": type_input})
    double = c.fetchone()
    double_type = c.fetchone()
    if double == None:
        c.execute("insert into table1 (name, num,type) values (?, ?,?)",(name_input,num_input,type_input))
          
    else:
        c.execute("UPDATE table1 set num=? WHERE name=?",(int(num_input),name_input))
        
