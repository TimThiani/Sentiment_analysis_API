from app.utils import analyze_sentiment

def perform_sentiment_analysis(text: str) -> str:
    """Analyzes the sentiment of the given text."""
    return analyze_sentiment(text)
