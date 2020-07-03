import sqlite3
import db_setup_handler

def create_tactics(cursor):
  try:
    cursor.execute("""CREATE TABLE tactics
                  (id INTEGER, fen TEXT, rating int, to_move TEXT, solution TEXT)""")
  except:
    pass

db_setup_handler.connect("tactics.db", create_tactics)
