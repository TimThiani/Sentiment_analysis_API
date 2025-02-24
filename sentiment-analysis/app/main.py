from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Sentiment Analysis API",
    description="API for analyzing sentiment in text",
    version="1.0.0"
)

# Register routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to Sentiment Analysis API"}
