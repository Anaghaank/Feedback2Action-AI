import sys
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Add the parent directory (feedback2action-ai) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import load_and_clean_data, analyze_sentiment, classify_topics  # Import from app

def main():
    st.title("Customer Feedback Analysis Dashboard")

    # File upload section
    uploaded_file = st.file_uploader("Upload your feedback file", type=["csv", "txt"])
    
    if uploaded_file is not None:
        try:
            # Load and process the uploaded file
            df = pd.read_csv(uploaded_file)
            st.write("Data Sample:", df.head())  # Display a sample of the uploaded data

            # Assuming the feedback data has a 'text' column
            if 'text' in df.columns:
                # Clean and analyze the feedback data
                cleaned_data = load_and_clean_data(df)
                sentiment_results = analyze_sentiment(cleaned_data)
                topic_results = classify_topics(sentiment_results)
                
                # Combine Sentiment and Topic into one table
                combined_data = topic_results[['text', 'sentiment', 'confidence', 'topic', 'topic_confidence']]

                # Display the combined table
                st.subheader("Sentiment & Topic Analysis")
                st.write(combined_data)

                # Independent Visualization: Sentiment Distribution
                sentiment_filter = st.selectbox("Select Sentiment to Filter for Sentiment Distribution", options=["All", "POSITIVE", "NEGATIVE", "NEUTRAL"])
                filtered_sentiment_data = combined_data[combined_data['sentiment'] == sentiment_filter] if sentiment_filter != "All" else combined_data
                
                st.subheader(f"📊 Sentiment Distribution ({sentiment_filter})")
                fig1, ax1 = plt.subplots()
                sns.countplot(data=filtered_sentiment_data, x='sentiment', ax=ax1)
                st.pyplot(fig1)

                # Independent Visualization: Topic Distribution
                topic_filter = st.selectbox("Select Topic to Filter for Topic Distribution", options=["All", "Delivery Issue", "Customer Support", "UX/UI", "Pricing", "General"])
                filtered_topic_data = combined_data[combined_data['topic'] == topic_filter] if topic_filter != "All" else combined_data

                st.subheader(f"📊 Topic Distribution ({topic_filter})")
                fig2, ax2 = plt.subplots(figsize=(10, 4))
                sns.countplot(data=filtered_topic_data, y='topic', order=filtered_topic_data['topic'].value_counts().index, ax=ax2)
                st.pyplot(fig2)

                # Independent Visualization: Topic vs Sentiment Heatmap
                sentiment_for_heatmap = st.selectbox("Select Sentiment to Filter for Heatmap", options=["All", "POSITIVE", "NEGATIVE", "NEUTRAL"])
                topic_for_heatmap = st.selectbox("Select Topic to Filter for Heatmap", options=["All", "Delivery Issue", "Customer Support", "UX/UI", "Pricing", "General"])

                # Filter data based on selected options for Heatmap
                filtered_heatmap_data = combined_data
                if sentiment_for_heatmap != "All":
                    filtered_heatmap_data = filtered_heatmap_data[filtered_heatmap_data['sentiment'] == sentiment_for_heatmap]
                if topic_for_heatmap != "All":
                    filtered_heatmap_data = filtered_heatmap_data[filtered_heatmap_data['topic'] == topic_for_heatmap]

                st.subheader(f"📊 Topic vs Sentiment Heatmap ({sentiment_for_heatmap}, {topic_for_heatmap})")
                heatmap_data = filtered_heatmap_data.groupby(['topic', 'sentiment']).size().unstack(fill_value=0)

                # Ensure we have the proper order for visualization
                fig3, ax3 = plt.subplots(figsize=(8, 6))
                sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu", ax=ax3, linewidths=.5)
                st.pyplot(fig3)

                # Download button for processed data
                st.subheader("📥 Download Processed Data")
                csv = combined_data.to_csv(index=False)
                st.download_button(
                    label="Download Summary CSV",
                    data=csv,
                    file_name='feedback_summary.csv',
                    mime='text/csv',
                )
                
            else:
                st.error("The uploaded file does not contain a 'text' column.")

        except Exception as e:
            st.error(f"❌ Error processing file: {str(e)}")
            st.text("Please ensure the file is in the correct format.")
            

if __name__ == "__main__":
    main()
