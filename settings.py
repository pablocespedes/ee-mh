import os

mongo_uri = str(os.environ.get("DB", "mongodb://localhost:27017/"))
mongo_db_name = str(os.environ.get("DB_NAME", "eateasy-testing"))
port = int(os.environ.get("PORT", 5000))
