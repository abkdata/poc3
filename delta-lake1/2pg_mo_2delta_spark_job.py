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

# PostgreSQL configuration
jdbc_url = "jdbc:postgresql://<postgresql_host>:<postgresql_port>/<database_name>"
jdbc_properties = {
    "user": "<postgresql_user>",
    "password": "<postgresql_password>",
    "driver": "org.postgresql.Driver"
}

# Read data from PostgreSQL
postgresql_df = spark.read.jdbc(jdbc_url, "<table_name>", properties=jdbc_properties)

# MongoDB configuration
mongodb_uri = "mongodb://<mongodb_user>:<mongodb_password>@<mongodb_host>:<mongodb_port>/<database_name>.<collection_name>"

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
