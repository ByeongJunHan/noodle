import sqlite3
name_input = input("새로 추가할 라면이름을 입력하세m ex)sin: ")
num_input = int(input("새로 추가할 라면수를 입력하세m ex)8: "))
type_input = input("새로 추가할 라면의 타입을 입력하세요ex)cup,bongzi : ")
def ramen_add(name_input,num_input,type_input):
    conn = sqlite3.connect("ramen.db", isolation_level=None)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS table1 \
        (name text, num interger, type text)")
    c.execute("SELECT num FROM table1 WHERE name=:Name", {"Name": name_input})
    double = c.fetchone()
    if double == None:
        c.execute("insert into table1 (name, num,type) values (?, ?,?)",(name_input,num_input,type_input))
    else:
        double = double[0]
        num1 = double + num_input
        c.execute("UPDATE table1 set num=? WHERE name=?",(num1,name_input))
