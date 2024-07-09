from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("Postgres to Delta Lake") \
    .config("spark.jars", "path_to_postgres_jdbc_driver.jar") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Define the JDBC properties
jdbc_url = "jdbc:postgresql://5432/customerdb"
jdbc_properties = {
    "user": "example",
    "password": "example",
    "driver": "org.postgresql.Driver"
}

# Read data from PostgreSQL
df = spark.read.jdbc(url=jdbc_url, table="cust_data", properties=jdbc_properties)

# Write data to Delta Lake
df.write.format("delta").save("/data/delta/your_table")

# Stop the Spark session
spark.stop()
