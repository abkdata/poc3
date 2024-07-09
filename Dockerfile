FROM bitnami/spark:3.2.0

# Add Delta Lake jar
RUN mkdir -p /opt/spark/jars
ADD https://repo1.maven.org/maven2/io/delta/delta-core_2.12/1.0.0/delta-core_2.12-1.0.0.jar /opt/spark/jars/

# Set environment variables for Delta Lake
ENV SPARK_CLASSPATH=/opt/spark/jars/delta-core_2.12-1.0.0.jar
ENV SPARK_SUBMIT_ARGS="--packages io.delta:delta-core_2.12:1.0.0 --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
