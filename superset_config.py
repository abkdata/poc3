import os

# Replace with a strong secret key
SECRET_KEY = 'bRNx64kfbRd/t+kY029Pa5fVSKE0Bnr30pmoWXE6qvE0xAVSJT70t5Dr'
# Generated in bash  command openssl rand -base64 42

# Database connection string
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://superset:superset@postgres:5432/superset'

# Superset specific config
SUPERSET_WEBSERVER_PORT = 8088
