import os

uri = "mongodb://eateasy-nyc:eateasy-nyc@ds053679-a0.mongolab.com:53679/eateasy"
mongo_uri = str(os.environ.get("DB", uri))
mongo_db_name = str(os.environ.get("DB_NAME", "eateasy"))
port = int(os.environ.get("PORT", 8080))
