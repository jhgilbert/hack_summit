#!/usr/bin/env python

from flask.ext.script import Manager
from hacksummit import app, db
from hacksummit.models import Loan, Lender, Loan_Lenders
import os

try:
  import simplejson as json
except ImportError:
  import json

manager = Manager(app)

@manager.command
def runserver():
  os.putenv('DATABASE_URL', app.config['SQLALCHEMY_DATABASE_URI'])
  db.create_all()
  app.run(host='0.0.0.0', debug=True)

@manager.command
def nuke_db():
  db.drop_all()
  db.create_all()

@manager.option('-f', '--file', dest='filename')
def load(filename):

  print "importing records from %s" % filename


  fh = open(filename, 'r')
  raw_json = json.load(fh)
  fh.close()

  for record in raw_json['loans']:
    if record['status'] == 'paid':
      print "...skipping, it's paid"
      continue


    model = Loan()

    for key in record:
      if hasattr(model, key):
        setattr(model, key, record[key])

    if hasattr(model, 'json'):
      setattr(model, 'json', json.dumps(record))

    db.session.add(model)

  db.session.commit()

if __name__ == "__main__":
    manager.run()
