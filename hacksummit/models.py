from database import DatabaseModel, db
from sqlalchemy import Column, Integer, String, BLOB, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

# junction table for
lender_friends = db.Table('friends',
  db.Column('lender_id', db.Integer, db.ForeignKey('lenders.id'), primary_key=True),
  db.Column('friend_id', db.Integer, db.ForeignKey('lenders.id'), primary_key=True)
)

class Loan(DatabaseModel):
  __tablename__ = 'loans'
  id = Column(Integer, primary_key=True)
  json = Column(BLOB, doc="Raw JSON blob")

class Lender(DatabaseModel):
  __tablename__ = 'lenders'

  id = Column(Integer, primary_key=True)
  facebook_id = Column(String(200), unique=True)
  work = Column(String(200))
  location = Column(String(200))
  hometown = Column(String(200))
  username = Column(String(200), unique=True)
  json = Column(BLOB, doc="Raw JSON blob")

  friends = relationship('Lender', secondary=lender_friends,
                        primaryjoin="lenders.c.id==friends.c.lender_id",
                        secondaryjoin="lenders.c.id==friends.c.friend_id",
                        backref='friends_with'
  )

class Loan_Lenders(DatabaseModel):
  __tablename__ = 'loan_lenders'

  id = Column(Integer, primary_key=True)
  json = Column(BLOB, doc="Raw JSON blob")

class Recommendation(DatabaseModel):
  __tablename__ = 'recommendations'

  id = Column(Integer, primary_key=True)
  lender_id = Column(Integer)
  loan_id = Column(Integer)
  score = Column(Integer)
  json = Column(BLOB, doc="Raw JSON blob")

