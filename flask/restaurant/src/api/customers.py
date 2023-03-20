from flask import Blueprint, jsonify, abort, request
from ..models import Cashier, Customer, Bill, Order, Item, db

bp = Blueprint('customers', __name__, url_prefix='/customers')


@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    customers = Customer.query.all() # ORM performs SELECT query
    result = []
    for c in customers:
        result.append(c.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

