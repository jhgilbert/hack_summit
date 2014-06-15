from flask import Flask, jsonify
from flask.ext.heroku import Heroku

from database import db
from models import Loan, Lender

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

@app.route('/lender/')
def all_lenders():
  result = ""

  for lender in Lender.query.all():
    result += "<p>%s</p>" % lender.username

  return result


@app.route('/lender/<username>')
def lender(username):

  user = db.session.query(Lender).filter(Lender.username==username).first()

  if user:
    return "This user (%s) already exists!" % user.username

  # create new user and save the username
  user = Lender()
  user.username = username
  user.save()

  return "hi %s, you have been created" % user.username