import sqlite3
import db_setup_handler

def reset_users(cursor):
  try:
    cursor.execute("""DELETE FROM users""")
  except:
    pass

def reset_user_stats(cursor):
  try:
    cursor.execute("""DELETE FROM user_stats""")
  except:
    pass

db_setup_handler.connect("users.db", reset_users, reset_user_stats)

