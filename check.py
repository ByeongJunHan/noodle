import sqlite3
import threading

def check_all():
  conn = sqlite3.connect("ramen.sqlite", isolation_level=None)
  #get  커서 
  c = conn.cursor()
    # 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
  c.execute("CREATE TABLE IF NOT EXISTS table1 \
  (name text, num interger, type text)")
  c.execute("SELECT * FROM table1")
  global all_ramen
  global all_name
  global all_num
  global all_type
  all_ramen = c.fetchall()
  for i in range(len(all_ramen)):
    all_name = all_ramen[i][0]
    all_num = all_ramen[i][1]
    all_type = all_ramen[i][2]
    

  threading.Timer(3, check_all).start()
check_all()
def ramen_check(name_input,type_input):
    c.execute("SELECT num FROM table1 WHERE name=:Name AND type=:Type", {"Name": name_input,"Type":type_input})
    double = c.fetchone()
    if double == None:
        print("아무 정보가 없는 라면입니다! 추가한후 다시오세요!")
    else:
        global ramen_num 
        ramen_num = double[0]
