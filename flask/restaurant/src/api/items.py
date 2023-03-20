from flask import Blueprint, jsonify, abort, request
from ..models import Cashier, Customer, Bill, Order, Item, db

bp = Blueprint('items', __name__, url_prefix='/items')


@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    items = Item.query.all() # ORM performs SELECT query
    result = []
    for o in items:
        result.append(o.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response