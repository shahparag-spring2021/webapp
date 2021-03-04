import os

db_name = os.environ['RDS_DB_NAME']
db_endpoint = os.environ['RDS_DB_ENDPOINT']
db_username = os.environ['RDS_DB_USERNAME']
db_password = os.environ['RDS_DB_PASSWORD']
s3_bucketname = os.environ['S3_BUCKET_NAME']

# db_name = 'webapp'
# db_endpoint = 'localhost:5432'
# db_username = 'postgres'
# db_password = 'admin123'

# SECRET_KEY = 'CSYE6225 Big Secret Key to create a webapp'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///webapp.sqlite'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@localhost/webapp'
SECRET_KEY = os.environ['SECRET_KEY']
SQLALCHEMY_DATABASE_URI = 'postgresql://'+db_username+':'+db_password+'@'+db_endpoint+'/'+db_name
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# print(SQLALCHEMY_DATABASE_URI)
# print(SQLALCHEMY_DATABASE_URI_TEST)
