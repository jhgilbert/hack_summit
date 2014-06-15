from __future__ import division
from flask import jsonify, request, g
from ..models import Loan, Lender
import random
import math
try:
  import simplejson as json
except ImportError:
  import json


def get_fractional(list_size, percentage):
  return math.ceil(list_size * (percentage / 100))

def get_limit(default=10):
  limit = request.args.get('limit', None)

  try:
    limit = int(limit) or 1
  except (ValueError, TypeError): #not a number or None
    limit = default

  return limit


def jsonify_list(query):
  if hasattr(query, 'all'):
    item_list = query.all()
  else:
    item_list = query # list or other thing

  result = {
    "results" : [json.loads(item.json) for item in item_list]
  }

  return jsonify(result)


def get_x_random_items(query, limit=1):
  # in a real production env, I'd want to give all loans a random number
  # that this would select against, but this is good enough for our sample size
  return random.sample(query.all(), limit)

def get_staff_picks(limit=5):
  query = Loan.query.filter(Loan.is_staff_pick==True)
  return get_x_random_items(query, limit=limit)

def get_popular_picks(limit=5):
  query = Loan.query.order_by(Loan.popularity)
  return get_x_random_items(query, limit=limit)

def get_friend_picks(user=None, limit=5):
  if user is None:
    user = g.user


