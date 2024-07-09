import os
from pyspark.sql import SparkSession
from delta.tables import DeltaTable

# Create Spark session
spark = SparkSession.builder \
    .appName("Delta Lake Example") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.2.20,org.mongodb.spark:mongo-spark-connector_2.12:10.0.1") \
    .getOrCreate()

# Enable Delta Lake support
spark.conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
spark.conf.set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

# PostgreSQL configuration from environment variables
jdbc_url = f"jdbc:postgresql://{os.getenv('POSTGRESQL_HOST')}:{os.getenv('POSTGRESQL_PORT')}/{os.getenv('POSTGRESQL_DB')}"
jdbc_properties = {
    "user": os.getenv('example'),
    "password": os.getenv('example'),
    "driver": "org.postgresql.Driver"
}

# Read data from PostgreSQL
postgresql_df = spark.read.jdbc(jdbc_url, "customerdb/cust_data", properties=jdbc_properties)

# MongoDB configuration from environment variables
mongodb_uri = f"mongodb://{os.getenv('27017')}:{os.getenv('27017')}/{os.getenv('mongodb_cust_evnt')}.{os.getenv('collect_cust_evnt')}"

# Read data from MongoDB
mongodb_df = spark.read.format("mongo").option("uri", mongodb_uri).load()

# Write the PostgreSQL DataFrame to Delta Lake
postgresql_df.write.format("delta").mode("overwrite").save("/tmp/delta-table-postgresql")

# Write the MongoDB DataFrame to Delta Lake
mongodb_df.write.format("delta").mode("overwrite").save("/tmp/delta-table-mongodb")

# Read and show the Delta tables
delta_postgresql_df = spark.read.format("delta").load("/tmp/delta-table-postgresql")
delta_postgresql_df.show()

delta_mongodb_df = spark.read.format("delta").load("/tmp/delta-table-mongodb")
delta_mongodb_df.show()
