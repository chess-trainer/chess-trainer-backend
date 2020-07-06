import sqlite3
import db_setup_handler

def create_users(cursor):
  try:
    cursor.execute("""CREATE TABLE users
                  (id INTEGER, username TEXT, password TEXT, email TEXT)""")
  except:
    pass

def create_user_stats(cursor):
  try:
    cursor.execute("""CREATE TABLE user_stats
                  (id INTEGER, 
                   visual_tactics_rating INTEGER)""")
  except:
    pass

db_setup_handler.connect("users.db", create_users, create_user_stats)
