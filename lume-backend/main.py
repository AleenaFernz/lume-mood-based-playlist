from fastapi import FastAPI
from routers import mood, playlist, profile

app = FastAPI()

app.include_router(mood.router)
app.include_router(playlist.router)
app.include_router(profile.router)

@app.get("/")
def root():
    return{"message": "Lume backend is running!!"}
