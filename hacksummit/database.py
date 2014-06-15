from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DatabaseModel(db.Model):
  __abstract__ = True

  def save(self):
    db.session.add(self)
    db.session.commit()
    return self
