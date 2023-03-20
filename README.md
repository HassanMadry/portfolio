# portfolio
Title: Mini Resturant Mangement System

Description:
Mini Restaurant Management System
This code represents a mini restaurant management system built with Flask SQLAlchemy.
 It consists of several database models that represent different aspects of a restaurant such as customers, items, orders, bills, cashiers, and order items.

The Customer model stores customer information such as their name, contact, and bills.
The Item model stores item information such as its name, price, and quantity. 
The Order model represents an order placed by a customer, which includes the order number, the customer ID, the number of items ordered, and the item number. 
The Bill model stores information about a customer's bill, which includes the bill number, the order number, the total price, and the customer ID. 
The OrderItem model represents a many-to-many relationship between orders and items. The Cashier model stores information about the cashier who processed the bill, which includes their name and the bill number.

Each model has a serialize method that returns a dictionary representation of the object, which can be useful for JSON serialization.

Overall, this system provides a way to manage orders, bills, and customers in a restaurant setting.


------------------------------------------------------------------------------------
| Endpoint Path|   Method    |                    Description                      |
| ------------ | ----------- | ----------------------------------------------------|
| /casheirs    | GET         |  Retrieve all cashiers with order id                |
| /items       | GET         |  Retrieve all items with thier prices and quantity  |
| /orders      | GET         |  Retrieve orders, customer name, item, price        |
| /bills       | Text        |  Retrieve bill, customer, order, price              |
------------------------------------------------------------------------------------


The project evolve over time. Since week one, I had clear plan, and I know what I wanted to do. So I first learned the tools needed,
then I started working on the project. I only revised it once when I was working on the ER Diagram. I choosed the ORM method because I think 
it has many tools which can allow you to do a lot and can save you a lot of headich if you do it the right way. 

I'm thinking to expand this project and create a front-end just for fun