from flask.ext.script import Manager
from hacksummit import app

manager = Manager(app)

@manager.command
def runserver():
    app.run(host='0.0.0.0', debug=True)

if __name__ == "__main__":
    manager.run()