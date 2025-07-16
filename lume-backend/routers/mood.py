from fastapi import APIRouter

router = APIRouter()

@router.post("/mood-detect")
def detect_mood():
    return {"mood": "Happy"} #Dummy response