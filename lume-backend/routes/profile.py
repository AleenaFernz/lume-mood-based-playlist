from fastapi import APIRouter

router = APIRouter()

@router.get("/profile")
def get_profile():
    return {"user": "example_user", "history": []} #dummy response