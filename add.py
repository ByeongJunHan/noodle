import sqlite3
def ramen_add(name_input,num_input,type_input):
    conn = sqlite3.connect("ramen.sqlite", isolation_level=None)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS table1 \
        (name text, num interger, type text)")
    c.execute("SELECT num FROM table1 WHERE name=:Name", {"Name": name_input})
    double = c.fetchone()
    c.execute("SELECT num FROM table1 WHERE type=:Type", {"Type": type_input})
    double_type = c.fetchone()
    if double == None:
        c.execute("insert into table1 (name, num,type) values (?, ?,?)",(name_input,num_input,type_input))
    if double_type == None:
        c.execute("insert into table1 (name, num,type) values (?, ?,?)",(name_input,num_input,type_input))
          
    else:
        double = double[0]
        num1 = double + int(num_input)
        c.execute("UPDATE table1 set num=? WHERE name=?",(num1,name_input))
ramen_add("sin",7,"bongzi")
        
