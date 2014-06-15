from flask import Flask, jsonify
from flask.ext.heroku import Heroku

from database import db
from models import Loan

app = Flask(__name__)
app.config.from_object('hacksummit.default_config')

heroku = Heroku(app)

db.app = app
db.init_app(app)

db.create_all()

@app.route('/')
def hello():
  return 'Hello World!'

@app.route('/loan/')
def all_loans():
  count = db.session.query(Loan).count()
  return "There are %s loans in the db" % count

@app.route('/loan/<int:loan_id>')
def loan(loan_id):
  loan = Loan.query.get_or_404(loan_id)
  return loan.json


