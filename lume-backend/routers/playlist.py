from fastapi import APIRouter

router = APIRouter()

@router.get("/playlist")
def get_playlist():
    return {"playlist": ["song1", "song2"]}  #Dummy response
