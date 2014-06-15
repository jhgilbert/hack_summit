from database import DatabaseModel
from sqlalchemy import Column, Integer, String, BLOB, DateTime, ForeignKey
from sqlalchemy.orm import relationship

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

