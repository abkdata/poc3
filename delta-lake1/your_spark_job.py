from pyspark.sql import SparkSession
from delta.tables import DeltaTable

# Create Spark session
spark = SparkSession.builder \
    .appName("Delta Lake Example") \
    .getOrCreate()

# Enable Delta Lake support
spark.conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
spark.conf.set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

# Create a DataFrame
data = [(1, 'foo'), (2, 'bar')]
df = spark.createDataFrame(data, ["id", "value"])

# Write the DataFrame as a Delta table
df.write.format("delta").save("/tmp/delta-table")

# Read the Delta table
delta_df = spark.read.format("delta").load("/tmp/delta-table")
delta_df.show()

# Perform update
delta_table = DeltaTable.forPath(spark, "/tmp/delta-table")
delta_table.update(
  condition = "id == 1",
  set = { "value": "'updated_value'" }
)

# Perform delete
delta_table.delete(condition = "id == 2")

# Show the updated Delta table
delta_df = spark.read.format("delta").load("/tmp/delta-table")
delta_df.show()
