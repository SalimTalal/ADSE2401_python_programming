# Python script to demonstrate connecting a Python app to MongoDB.
# NB: Ensure that the mongodb driver is installed (pip install pymongo)
from bson import ObjectId
# Import the required modules
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client["ADSE-Restaurant"]

menu_col = db["menu"]
customers_col = db["customers"]
orders_col = db["orders"]

# -----------------------------------------------
# CREATE OPERATIONS
# ===============================================

# Function to add a menu item
def add_menu_item():
    item = {
        "name":"Pizza",
        "category":"Food",
        "sizes":[
            {"size":"small","price_kes":500},
            {"size":"medium","price_kes":800},
            {"size":"large","price_kes":1200}
        ]
    }
    result = menu_col.insert_one(item)
    print(f"Menu item with id: {result.inserted_id} successfully added!")

def add_customer(name,phone,email):
    customer = {
        "name":name,
        "phone":phone,
        "email":email
    }
    result = customers_col.insert_one(customer)
    print(f"Customer with id: {result.inserted_id} successfully added!")
    return result.inserted_id

def create_order(customer_id):
    order = {
        "customer_id":customer_id,
        "items":[
            {
                "name":"Pizza",
                "size":"medium",
                "quantity":1,
                "price":800
            }
        ],
        "total_kes": 500,
        "status":"pending",
        "created_at":datetime.utcnow(),
    }
    result = orders_col.insert_one(order)
    print(f"Order with id: {result.inserted_id} successfully created!")

# -----------------------------------------------
# READ OPERATIONS
# ===============================================
def view_menu():
    print(f"\nMenu:")
    for item in menu_col.find():
        print(item)

def view_customers():
    print(f"\nCustomers:")
    for customer in customers_col.find():
        print(customer)

def view_orders():
    print(f"\nOrders:")
    for order in orders_col.find():
        print(order)

# -----------------------------------------------
# UPDATE OPERATIONS
# ===============================================
def update_order_status(order_id,new_status):
    result = orders_col.update_one(
        {"_id": order_id},
        {"$set":{"status":new_status}}
    )
    print(f"Orders updated: {result.modified_count}")

# -----------------------------------------------
# DELETE OPERATIONS
# ===============================================
def delete_customer(customer_id):
    result = customers_col.delete_one({"_id": ObjectId(customer_id)})
    print(f"Customer deleted: {result.deleted_count}")

# -----------------------------------------------
# ENTRY POINT TO OUR APPLICATION
# ===============================================
if __name__ == "__main__":
    # 1. Add a menu item
    #add_menu_item()

    #2. Add a customer
    #customer_id = add_customer("Alice","0751234598","alice@email.com")

    # 3. Create an order
    #create_order("69c76340ec312a53366bb78c")

    # NB: For update/delete, copy an ID from print out and then paste it below
    # 4. Delete Alice's record
    delete_customer("69c7de5ffab4b44f25b29924")

    # 5. Read data
    view_menu()
    view_customers()
    view_orders()

