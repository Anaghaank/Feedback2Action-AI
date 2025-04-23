import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(df):
    plt.figure(figsize=(6,4))
    sns.countplot(x='sentiment', data=df, palette='Set2')
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_topic_distribution(df):
    plt.figure(figsize=(8,4))
    sns.countplot(x='topic', data=df, palette='Set3')
    plt.title("Topic Distribution")
    plt.xlabel("Topic")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_topic_sentiment(df):
    plt.figure(figsize=(8,4))
    sns.barplot(data=df, x='topic', y='confidence', hue='sentiment', palette='Set1')
    plt.title("Average Sentiment Confidence by Topic")
    plt.xlabel("Topic")
    plt.ylabel("Confidence")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
