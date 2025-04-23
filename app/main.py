import pandas as pd
import re
from transformers import pipeline
from visualization import (
    plot_sentiment_distribution,
    plot_topic_distribution,
    plot_topic_sentiment,
)

# Load and clean data
def load_and_clean_data(filepath_or_df):
    if isinstance(filepath_or_df, str):
        df = pd.read_csv(filepath_or_df)
    else:
        df = filepath_or_df.copy()

    # Basic cleaning
    df["cleaned_text"] = df["text"].apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", str(x).lower()))
    return df
# Sentiment analysis
def analyze_sentiment(df):
    sentiment_analyzer = pipeline("sentiment-analysis")
    results = sentiment_analyzer(df["cleaned_text"].tolist())

    df["sentiment"] = [r["label"] for r in results]
    df["confidence"] = [round(r["score"], 2) for r in results]
    return df

# Simple rule-based topic classifier using keywords
def classify_topics(df):
    def get_topic(text):
        if any(word in text for word in ["delay", "late", "wait"]):
            return "Delivery Issue", 0.85
        elif any(word in text for word in ["support", "help", "customer service"]):
            return "Customer Support", 0.84
        elif any(word in text for word in ["interface", "design", "layout"]):
            return "UX/UI", 0.73
        elif any(word in text for word in ["price", "cost", "expensive"]):
            return "Pricing", 0.80
        else:
            return "General", 0.70

    df[["topic", "topic_confidence"]] = df["cleaned_text"].apply(lambda x: pd.Series(get_topic(x)))
    return df

# MAIN EXECUTION
if __name__ == "__main__":
    print("Device set to use cpu")

    filepath = "app/data/sample_feedback.csv"
    data = load_and_clean_data(filepath)

    print("\nData Sample:")
    print(data.head())

    data = analyze_sentiment(data)
    data = classify_topics(data)

    print("\nFinal Data with Sentiment and Topics:")
    print(data[["text", "sentiment", "confidence", "topic", "topic_confidence"]])

    # Generate Visualizations
    plot_sentiment_distribution(data)
    plot_topic_distribution(data)
    plot_topic_sentiment(data)
