from flask import Flask

app = Flask(__name__)

@app.route("/new_tactic/", methods=["GET"])
def new_tactic(rating):
  rating = request.args.get("rating", default=1600, type=int)
  return False 
