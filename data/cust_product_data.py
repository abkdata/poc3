from faker import Faker
import csv
import random

# Initialize Faker
fake = Faker()

# Generate customer product data
customer_products = []

for _ in range(10000):
    start_date = fake.date_this_decade()
    end_date = fake.date_between(start_date=start_date, end_date='today')
    customer_product = {
        "id": random.randint(200000, 299999),
        "customer_id":random.randint(300000, 399999),
        "product_id": random.randint(100000, 199999),
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat() if random.choice([True, False]) else None,
        "amount_invested": round(random.uniform(1000.0, 100000.0), 2),
        "active": random.choice([True, False])
    }
    customer_products.append(customer_product)

# Define the CSV file name
csv_file = 'customer_products.csv'

# Write the data to a CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "customer_id", "product_id", "start_date", "end_date", "amount_invested", "active"])
    writer.writeheader()
    writer.writerows(customer_products)

print(f'CSV file "{csv_file}" with 10K customer product records has been created.')
