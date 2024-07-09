docker run --name delta-lake-spark-container \
  -e POSTGRESQL_HOST=<5432> \
  -e POSTGRESQL_PORT=<5432> \
  -e POSTGRESQL_DB=<customerdb> \
  -e POSTGRESQL_USER=<example> \
  -e POSTGRESQL_PASSWORD=<example> \
  -e MONGODB_HOST=<27017> \
  -e MONGODB_PORT=<27017> \
  -e MONGODB_DB=<mongodb_cust_evnt> \
  -e MONGODB_COLLECTION=<collect_cust_evnt> \
#   -e MONGODB_USER=<mongodb_user> \
#   -e MONGODB_PASSWORD=<mongodb_password> \
  delta-lake-spark
