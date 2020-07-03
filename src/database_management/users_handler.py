import rand

import db_handler as db

min_id = 100000000000
max_id = 999999999999

def new_user(username, password, email):
  user_columns = ("id", "username", "password", "email")
  user_stats_columns = ("id", "visual_tactics_rating")
  user_id = rand.randInt(min_id, max_id) 
  while len(db.select"users.db", "users", "*", "id=" + str(user_id)) != 0:
    user_id = rand.randInt(min_id, max_id)
  db.insert("users.db", "users", user_columns, (user_id, username, password, email)) 
  db.insert("users.db", "user_stats", user_stats_columns, (user_id, 1200)) 
