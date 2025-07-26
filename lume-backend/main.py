from fastapi import FastAPI
from services.db import users_collection
from routes.mood import router as mood_router  #imports our router

app = FastAPI()



@app.get("/mongo-test")
def mongo_test():
    count = users_collection.count_documents({})
    return{"user_count": count}

app.include_router(mood_router, prefix="/api") #Now api/detect-mood will work
