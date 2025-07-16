from pymongo import MongoClient #MongoClient is the object that connects fast api bacckend to mongodb
import os                       #built-in python module that lets you read environment variables
from dotenv import load_dotenv  #loads environment variables from a .env file

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client['lume_db']
users_collection = db['users']