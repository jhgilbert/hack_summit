from flask import Blueprint, jsonify, request
try:
  import simplejson as json
except ImportError:
  import json

from ..database import db
from ..models import Loan

this = Blueprint('api', __name__)

@this.route('/lender/picks', methods=["GET"])
def get_recommendations_for_user():
  limit = request.args.get('limit', None)

  try:
    limit = int(limit) or 1
  except (ValueError, TypeError): #not a number or None
    limit = 10

  loans = db.session.query(Loan).limit(limit).all()

  result = {
    "results" : [json.loads(item.json) for item in loans]
  }

  return jsonify(result)

