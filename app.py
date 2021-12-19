from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  from check import all_ramen
  return render_template("index.html",all_ramen=all_ramen)
@app.route('/change')
def change():
  from check import all_ramen
  return render_template("change.html",all_ramen=all_ramen)
  
@app.route('/add/<name>/<num>/<type>')
def add(name,num,type):
  import add
  add.ramen_add(name,num,type)
  return render_template("add.html",name=name,num=num,type=type)
@app.route('/check/<name>/<type>')
def check(name,type):
  import check
  check.ramen_check(name,type)
  from check import ramen_num
  print(ramen_num)
  return render_template("check.html",num = ramen_num,name = name,type=type)

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False,port='80',host='0.0.0.0')
