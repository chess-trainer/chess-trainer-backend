import sqlite3
import db_setup_handler

def reset_tactics(cursor):
  try:
    cursor.execute("""DELETE FROM tactics""")
  except:
    pass

db_setup_handler.connect("tactics.db", reset_tactics)

