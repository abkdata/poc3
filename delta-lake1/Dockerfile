# Use the official Spark image from Docker Hub
FROM bitnami/spark:latest

# Install necessary packages
RUN apt-get update && apt-get install -y openjdk-8-jdk wget && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH

# Download Delta Lake jars
RUN wget https://repo1.maven.org/maven2/io/delta/delta-core_2.12/1.0.0/delta-core_2.12-1.0.0.jar -P /opt/spark/jars/

# Copy your Spark job to the container
COPY your_spark_job.py /opt/spark/jobs/

# Define the entry point for the container
ENTRYPOINT [ "/opt/bitnami/scripts/spark/entrypoint.sh" ]
CMD [ "spark-submit", "--packages", "io.delta:delta-core_2.12:1.0.0", "/opt/spark/jobs/your_spark_job.py" ]
