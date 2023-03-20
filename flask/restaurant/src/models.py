from sqlalchemy import create_engine, Column, Integer, Numeric, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    customer_bills = relationship("Bill")

    def __init__(self, customer_id: int, name: str, contact: str):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact

    def serialize(self):
        return {
            'name': self.name,
            'contact': self.contact,
            'customer_id': self.customer_id
        }

class Item(db.Model):
    __tablename__ = 'items'

    item_no = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    quantity = Column(Integer, nullable=False)
    order_no = Column(Integer, nullable=False)

    def __init__(self, item_no = int, name = str, price = float, quantity = int):
        self.item_no = item_no
        self.name = name
        self.price = price
        self.quantity = quantity

    def serialize(self):
        return {
            'item_no': self.item_no,
            'name': self.name,
            'price': str(self.price),
            'quantity': self.quantity
        }
class Order(db.Model):
    __tablename__ = 'orders'

    order_no = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable=False)
    no_of_items = Column(Integer)
    item_no = Column(Integer, ForeignKey('items.item_no'), nullable=False)
    customer = relationship(Customer, backref=backref('orders', cascade='all, delete-orphan'))
    item = relationship(Item, backref=backref('orders', cascade='all, delete-orphan'))


    def __init__(self, order_no = int, customer_id=int, no_of_items = int, items= relationship):
        self.order_no = order_no
        self.customer_id = customer_id
        self.no_of_items = no_of_items
        self.items = items
    def serialize(self):
        return {
            'order_no': self.order_no,
            'no_of_items': self.no_of_items,
            'customer_id': self.customer.customer_id,
            'customer_name': self.customer.name, 
            'Item_name': self.item.name,
            'Item_price': str(self.item.price)
        }
class Bill(db.Model):
    __tablename__ = 'bills'

    bill_no = Column(Integer, primary_key=True)
    order_no = Column(Integer, ForeignKey('orders.order_no'), nullable=False)
    price = Column(Numeric, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable=False)
    customer = relationship(Customer, backref=backref('bills', cascade='all, delete-orphan'))
    order = relationship(Order, backref=backref('bills', cascade='all, delete-orphan'))
    

    def __init__(self, bill_no: int, order_no: int, price: float, customer_id: int):
        self.bill_no = bill_no
        self.order_no = order_no
        self.price = price
        self.customer_id = customer_id

    def serialize(self):
        return {
            'order_no': self.order_no,
            'bill_no': self.bill_no,
            'price': str(self.price),
            'customer_name': self.customer.name,
            'customer_contact': self.customer.contact
        }



class OrderItem(db.Model):
    __tablename__ = 'orders_items'

    item_no = Column(Integer, ForeignKey('items.item_no'), primary_key=True)
    order_no = Column(Integer, ForeignKey('orders.order_no'), primary_key=True)
    item = relationship(Item, backref=backref('order_items', cascade='all, delete-orphan'))
    order = relationship('Order', backref=backref('order_items', cascade='all, delete-orphan'))


class Cashier(db.Model):
    __tablename__ = 'cashiers'

    cashier_id = Column(Integer, primary_key=True)
    bill_no = Column(Integer, ForeignKey('bills.bill_no'), nullable=False)
    name = Column(String, nullable=False)
    bill = relationship(Bill, backref=backref('cashiers', cascade='all, delete-orphan'))

    def __init__(self, bill_no: int, name: str):
        self.bill_no = bill_no
        self.name = name
    
    def serialize(self):
        return {
            'cashier_id': self.cashier_id,
            'bill_no': self.bill_no,
            'name': self.name
        }