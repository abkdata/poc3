from faker import Faker
import csv
import random

# Initialize Faker
fake = Faker()

# Define product types
product_types = ['New Insurance', 'Insurance renew', 'Insurance update', 'Insurance migrate', 'Insurance claim']

# Generate product data
products = []

for i in range(1, 100):
    product = {
        "id": random.randint(100000, 199999),
        "name": f"Insu-Product#{random.randint(1, 5)}",
        "type": fake.random.choice(product_types)
    }
    products.append(product)

# Define the CSV file name
csv_file = 'products.csv'

# Write the data to a CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "type"])
    writer.writeheader()
    writer.writerows(products)

print(f'CSV file "{csv_file}" with 100 product records has been created.')
