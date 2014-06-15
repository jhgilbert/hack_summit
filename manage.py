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

@manager.option('-d', '--dir', dest='data_dir')
def import_data(data_dir):

  for ModelClass in [Loan]:
    model_name = ModelClass.__tablename__

    print "Importing records for %s" % model_name

    import_dir = os.path.join(data_dir, model_name)

    if not os.path.exists(import_dir):
      print "No fixture data exists for %s" % model_name
      continue

    LIMIT = 10
    current = 0
    for json_filename in os.listdir(import_dir):
      current += 1
      if current > LIMIT:
        break

      try:
        fh = open(os.path.join(import_dir, json_filename), 'r')
        raw_json = json.load(fh)
        fh.close()
      except IOError as e:
        print "Can't load file %s %s" % (json_filename, e)
        continue

      print "...%s" % json_filename

      for record in raw_json[model_name]:
        model = ModelClass()

        for key in record:
          if hasattr(model, key):
            setattr(model, key, record[key])

        if hasattr(model, 'json'):
          setattr(model, 'json', json.dumps(record))

        db.session.add(model)

    db.session.commit()

if __name__ == "__main__":
    manager.run()
