from fastapi import APIRouter #APIRouter is used to split API into modular parts (like routes for mood , users, etc......)
from models.mood import MoodRequest
from lume_nlp.model.mood_classifier import classify_mood

router = APIRouter()  # here we created an instance of the APIROuter ---- why ??? well from here on when we define anu routes using @router.get / @router.post will belong to this group

@router.post("/detect-mood")   #Create a post endpoint -> POST /detect-mood
def detect_mood(payload: MoodRequest):
    text = payload.text        #extracts the input text message

    #For now return dummy mood
    mood = classify_mood(text)
    return {"mood": mood}