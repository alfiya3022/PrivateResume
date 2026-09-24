from fastapi import FastAPI

from backend.app.config import APP_NAME


app = FastAPI(
    title=APP_NAME)


@app.get("/health")
def health_check():
    return {"status": "ok"}