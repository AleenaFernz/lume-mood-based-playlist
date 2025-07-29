import sys
import os

# ✅ Add root and lume-nlp to PYTHONPATH
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)
sys.path.append(os.path.join(root_dir, "lume-nlp"))  # Enables importing lume_nlp.*

from fastapi import FastAPI
from services.db import users_collection
from routes.mood import router as mood_router  # Our custom mood detection route

app = FastAPI()


@app.get("/mongo-test")
def mongo_test():
    count = users_collection.count_documents({})
    return {"user_count": count}


# 🎯 All mood detection APIs will now be under /api
app.include_router(mood_router, prefix="/api")
