from faker import Faker
import json
import random
from pymongo import MongoClient

# Initialize Faker
fake = Faker()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]  # replace with your database name
collection = db["customers"]       # replace with your collection name

# Generate customer data
customers = []

for _ in range(10):
    customer = {
        "id": random.randint(300000, 399999),
        "name": fake.name(),
        "ssn": fake.ssn(),
        "dob": fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
        "start_date": fake.date_this_decade().isoformat(),
        "kyc_date": fake.date_this_year().isoformat(),
        "net_worth": round(random.uniform(1000.0, 1000000.0), 2)
    }
    customers.append(customer)

# Convert the generated data to JSON format
customer_json = json.dumps(customers, indent=4)

# Print the generated JSON data
print(customer_json)

# Optionally, write the JSON data to a file
with open('customers.json', 'w') as json_file:
    json_file.write(customer_json)

print(f'JSON data with 10 customer records has been created and saved to "customers.json".')

# Insert the generated data into MongoDB
collection.insert_many(customers)

print("Customer data has been inserted into MongoDB.")
