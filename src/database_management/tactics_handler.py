import random

import db_handler as db

RATING_RANGE = 200

def get_tactic(rating):
  # columns are: id, fen, rating, to_move, solution
  tactics = db.select("tactics.db", "tactics", "*", "WHERE abs(rating - " + str(rating) + ") < " + str(RATING_RANGE))
  return random.choice(tactics) 
