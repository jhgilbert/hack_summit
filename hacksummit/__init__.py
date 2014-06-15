from flask import Flask
from flask.ext.heroku import Heroku

from database import db

app = Flask(__name__)
app.config.from_object('hacksummit.default_config')

heroku = Heroku(app)

db.app = app
db.init_app(app)

@app.route('/')
def hello():
  return 'Hello World!'




