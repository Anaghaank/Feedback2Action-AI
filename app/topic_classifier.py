from transformers import pipeline

# Define your topic labels
TOPIC_LABELS = ["Product", "Delivery", "Support", "User Experience", "Pricing", "Other"]

# Load the zero-shot classifier
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_topic(text, labels=TOPIC_LABELS):
    result = classifier(text, labels)
    return result['labels'][0], round(result['scores'][0], 2)  # Top label and score
