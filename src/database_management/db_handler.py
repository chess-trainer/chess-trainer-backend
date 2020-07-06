import sqlite3

def insert(db_name, table, columns, args):
  db_path = "../../storage/"+ db_name
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  sql = "INSERT INTO " + table + totuple(columns) + " VALUES" + qmark_args(len(args))
  cursor.execute(sql, args)
  conn.commit()
  result = cursor.lastrowid
  cursor.close()
  return result

def update(db_name, table, what, conditions):
  db_path = "../../storage/"+ db_name
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()  
  sql = "UPDATE " + table + " SET " + what + " " + conditions
  cursor.execute(sql)
  conn.commit()
  result = cursor.lastrowid
  cursor.close()
  return result 

def select(db_name, table, what, conditions):
  db_path = "../../storage/"+ db_name
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()  
  res = cursor.execute("SELECT " + what + " FROM " + table + " " + conditions)
  result = res.fetchall()
  cursor.close()  
  return result

def qmark_args(num):
  s = '('
  for i in range(num - 1):
    s += '?,'
  return s + '?)'

def totuple(args):
  s = '('
  for arg in args:
    s += arg + ','
  return s[:len(s)-1] + ')'
