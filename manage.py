#!/usr/bin/env python 

from flask.ext.script import Manager
from hacksummit import app, db
import alembic
import os

manager = Manager(app)

@manager.command
def runserver():
    os.putenv('DATABASE_URL', app.config['SQLALCHEMY_DATABASE_URI'])
    db.create_all()
    app.run(host='0.0.0.0', debug=True)

if __name__ == "__main__":
    manager.run()
