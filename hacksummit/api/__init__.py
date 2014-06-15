from flask import Blueprint, jsonify, request, g
from  sqlalchemy.sql.expression import func

import random

from ..database import db
from ..models import Loan

from .lib import *

this = Blueprint('api', __name__)

STAFF_PICK_PERCENT = 20
POPULAR_PERCENT = 20
FRIEND_ACTIVITY_PERCENT = 20
MAGIC_PERCENT = 40

@this.route('/lender/feed', methods=["GET"])
def current_user_integrated_feed():
  limit = get_limit()

  POPULAR_LIMIT = get_fractional(limit, POPULAR_PERCENT)
  FRIEND_LIMIT = get_fractional(limit, FRIEND_ACTIVITY_PERCENT)
  MAGIC_LIMIT = get_fractional(limit, MAGIC_PERCENT)

  staff_items = get_staff_picks(limit=get_fractional(limit, STAFF_PICK_PERCENT))
  popular_items = get_popular_picks(limit=get_fractional(limit, POPULAR_PERCENT))
  friend_limit = get_friend_picks(limit=get_fractional(limit, POPULAR_PERCENT))

@this.route('/loans/all', methods=["GET"])
def all_loans():
  query = db.session.query(Loan).order_by(func.random()).all()
  return jsonify_list(query)

@this.route('/lender/picks', methods=["GET"])
def current_user_recommended():
  query = db.session.query(Loan).order_by(func.random()).limit(get_limit())
  return jsonify_list(query)

@this.route('/staff/picks', methods=["GET"])
def staff_recommended():
  return jsonify_list(get_staff_picks(limit=get_limit()))

@this.route('/lender/friends/activity', methods=["GET"])
def current_user_friend_activity():
  pass

