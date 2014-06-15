from flask import Flask, jsonify, redirect, url_for, session, request
from flask.ext.heroku import Heroku
from flask_oauthlib.client import OAuth

from database import db
from models import Loan, Lender

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
app.config.from_object('hacksummit.default_config')

heroku = Heroku(app)

db.app = app
db.init_app(app)

db.create_all()

FACEBOOK_APP_ID = '524414764331163'
FACEBOOK_APP_SECRET = '5cc64ca9891c35fd651a7fea6d32c0ea'

oauth = OAuth(app)
facebook = oauth.remote_app('facebook',
  base_url='https://graph.facebook.com/',
  request_token_url=None,
  access_token_url='/oauth/access_token',
  authorize_url='https://www.facebook.com/dialog/oauth',
  consumer_key=FACEBOOK_APP_ID,
  consumer_secret=FACEBOOK_APP_SECRET,
  request_token_params={'scope': 'email,user_location,user_hometown,user_friends,user_work_history'}
)

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
    result += "<p>username=%s" % lender.username
    result += " : facebook_id=%s" % lender.facebook_id
    result += " : location=%s" % lender.location
    result += " : hometown=%s" % lender.hometown
    result += " : work=%s" % lender.work
    result += "</p>"

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


@app.route('/update_external_user_data')
def index():
  return redirect(url_for('oauth'))


@app.route('/oauth')
def oauth():
  return facebook.authorize(callback=url_for('facebook_authorized',
    next=request.args.get('next') or request.referrer or None,
    _external=True))


@app.route('/oauth/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
  if resp is None:
    return 'Access denied: reason=%s error=%s' % (
      request.args['error_reason'],
      request.args['error_description']
    )
  session['oauth_token'] = (resp['access_token'], '')

  me = facebook.get('/me')
  facebook_id = "%s" % me.data['id']

  user = db.session.query(Lender).filter(Lender.facebook_id==facebook_id).first()

  # If user doesn't exist, create him/her/it
  created = False
  if not user:
    user = Lender()
    created = True

  # Populate from user attributes
  user.facebook_id = facebook_id
  try:
    # only most frequent for ease of use during hackathon
    user.work = me.data['work'][0]['position']['name']
  except KeyError:
    pass
  try:
    user.location = me.data['location']['name']
  except KeyError:
    pass
  try:
    user.hometown = me.data['hometown']['name']
  except KeyError:
    pass

  # Populate from friends
  myfriends = facebook.get('/me/friends')

  user.save()

  # ???
  # g.user = user

  action = "created" if created else "updated"
  return "facebook_id %s %s" % (facebook_id, action)


@facebook.tokengetter
def get_facebook_oauth_token():
  return session.get('oauth_token')


@app.before_request
def before_request():
  # look in session for fb id,
  # then look in db
  # g.user = Lender

  pass

if __name__ == '__main__':
  app.run()
