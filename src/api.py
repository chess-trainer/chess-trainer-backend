from flask import Flask

import database_managemnet.tactics_handler as tactics_handler

app = Flask(__name__)

@app.route("/new_tactic/", methods=["GET"])
def new_tactic(rating):
  rating = request.args.get("rating", default=1600, type=int)
  return tactics_handler.get_tactic(rating) 
