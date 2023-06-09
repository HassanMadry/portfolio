from flask import Blueprint, jsonify, abort, request
from ..models import Cashier, Customer, Bill, Order, Item, db

bp = Blueprint('orders', __name__, url_prefix='/orders')


@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    orders = Order.query.all() # ORM performs SELECT query
    result = []
    for o in orders:
        result.append(o.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response