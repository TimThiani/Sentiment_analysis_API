from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    """Uses TextBlob to determine sentiment (positive, neutral, negative)."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"
    
    