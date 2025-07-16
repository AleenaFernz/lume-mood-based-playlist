from fastapi import FastAPI
from services.db import users_collection

app = FastAPI()



@app.get("/mongo-test")
def mongo_test():
    count = users_collection.count_documents({})
    return{"user_count": count}
