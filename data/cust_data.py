import csv
import random
from faker import Faker

fake = Faker()

# Generate 50 records
records = []
for _ in range(50000):
    record = {
        "id": random.randint(300000, 399999),
        "name": fake.name(),
        "ssn": fake.ssn(),
        "dob": fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
        "start_date": fake.date_this_decade().isoformat(),
        "kyc_date": fake.date_this_year().isoformat(),
        "net_worth": round(random.uniform(1000.0, 1000000.0), 2)
    }
    records.append(record)

# Define CSV file field names
fieldnames = ["id", "name", "ssn", "dob", "start_date", "kyc_date", "net_worth"]

# Write records to a CSV file
with open('customer_data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for record in records:
        writer.writerow(record)

print("50k records have been generated and saved to 'Customer_data.csv'.")
