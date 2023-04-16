import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('''create table if not exists employees(
                      id integer PRIMARY KEY, 
                      name text, 
                      salary real, 
                      department text, 
                      position text, 
                      hireDate text)''')
    con.commit()

def sql_insert(con, entities):
    cursorObj = con.cursor()   
    cursorObj.execute('INSERT INTO employees(name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?)', entities)   
    con.commit()

def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    con.commit()

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM employees')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

def sql_fetch2(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

def sql_list_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    print(cursorObj.fetchall())

# drop table if exists table_name
def sql_drop_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('DROP table if exists employees')
    con.commit()

con = sql_connection()
sql_table(con)

entities = ('Andrew', 800, 'IT', 'Tech', '2018-02-06')
sql_insert(con, entities)
sql_update(con)
sql_fetch(con)
sql_list_table(con)

con.close()