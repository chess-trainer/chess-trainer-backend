import db_handler_persistent as db

conn = None

def connect():
  global conn
  conn = db.connect("tactics.db")

def new_tactic(tactic_id, fen, rating, to_move, solution):
  global conn
  tactics_columns = ("id", "fen", "rating", "to_move", "solution")
  db.insert(conn, "tactics", tactics_columns, (tactic_id, fen, rating, to_move, solution)) 
