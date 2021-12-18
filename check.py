import sqlite3

def ramen_check(name_input):
    conn = sqlite3.connect("ramen.db", isolation_level=None)
    #get  커서 
    c = conn.cursor()
    # 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
    c.execute("CREATE TABLE IF NOT EXISTS table1 \
        (name text, num interger, type text)")
    c.execute("SELECT * FROM table1 WHERE name=:Name", {"Name": name_input})
    double = c.fetchone()
    if double == None:
        print("아무 정보가 없는 라면입니다! 추가한후 다시오세요!")
    else:
        ramen_num = double[1]
        c.execute("SELECT type FROM table1 WHERE name=:Name", {"Name": name_input})
        ramen_type = double[2]
