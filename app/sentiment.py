from transformers import pipeline

# Load sentiment analysis pipeline (only once)
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text[:512])[0]  # Truncate long text
    return result['label'], round(result['score'], 2)
