from fastapi import APIRouter, Depends
from app.schemas import TextRequest, SentimentResponse
from app.services import perform_sentiment_analysis

router = APIRouter()

@router.post("/analyze", response_model=SentimentResponse)
async def analyze_text(request: TextRequest):
    result = perform_sentiment_analysis(request.text)
    return {"text": request.text, "sentiment": result}
