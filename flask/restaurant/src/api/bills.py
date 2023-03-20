from flask import Blueprint, jsonify, abort, request
from ..models import Cashier, Customer, Bill, Order, Item, db

bp = Blueprint('bills', __name__, url_prefix='/bills')


@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    bills = Bill.query.all() # ORM performs SELECT query
    result = []
    for b in bills:
        result.append(b.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

