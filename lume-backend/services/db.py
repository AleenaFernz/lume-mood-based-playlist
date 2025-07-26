from pymongo import MongoClient
import os
from dotenv import load_dotenv
import certifi

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL, tls=True, tlsCAFile=certifi.where())
db = client["lume_db"]
users_collection = db["users"]
