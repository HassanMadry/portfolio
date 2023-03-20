from flask import Blueprint, jsonify, abort, request
from ..models import Cashier, Customer, Bill, Order, Item, db

bp = Blueprint('cashiers', __name__, url_prefix='/cashiers')


@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    cashiers = Cashier.query.all() # ORM performs SELECT query
    result = []
    for c in cashiers:
        result.append(c.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response