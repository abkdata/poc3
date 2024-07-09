from faker import Faker
from pymongo import MongoClient
import random

# Initialize Faker
fake = Faker()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mongodb_cust_evnt"]  # replace with your database name
collection = db["collect_cust_evnt"]  # replace with your collection name

# Define possible values for the fields
kyc_status_options = ["Pending", "Verified", "Rejected"]
prod_purchased_options = ["Product_A", "Product_B", "Product_C", "Product_D"]
purchase_mode_options = ["Online", "In-Store"]
cancellation_status_options = ["Cancelled", "Not Cancelled"]
special_remarks_options = [
    "High priority customer",
    "Frequent buyer",
    "Requires follow-up",
    "Special discount applied",
    "No special remarks"
]

# Generate customer data
customers = []

for _ in range(1000):
    customer = {
        "cust_id": random.randint(300000, 399999),
        "Customer": fake.name(),
        "KYC_Status": random.choice(kyc_status_options),
        "Prod_Purchased": random.choice(prod_purchased_options),
        "Purchase_mode": random.choice(purchase_mode_options),
        "Cancellation_Status": random.choice(cancellation_status_options),
        "Special_Remarks": random.choice(special_remarks_options)
    }
    customers.append(customer)

# Insert the generated data into MongoDB
collection.insert_many(customers)

print("1000 customer records have been inserted into MongoDB.")
