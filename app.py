from flask import Flask
from sqlite3 import sqlite3 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,world!'

 
conn= sqlite3.connect('database.db')
cursor.execute('CREATE TABLE IF NOT EXIST example(id INTERGER PRIMARY KEY, name TEXT)')
conn.comit()
conn.close() 

if __name__ == '__main__':
    app.run(debug=True)

