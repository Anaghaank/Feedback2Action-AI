
# **Feedback2Action-AI: Customer Feedback Analysis Tool**

Welcome to **Feedback2Action-AI**, an AI-powered platform that analyzes customer feedback using Natural Language Processing (NLP) techniques. This project processes customer feedback, extracts insights, and provides interactive visualizations to help businesses better understand and act upon customer opinions.

---

## 🚀 **Features**

- **Sentiment Analysis**: Automatically classifies customer feedback into different sentiment categories: Positive, Neutral, or Negative.
- **Topic Classification**: Categorizes feedback into predefined topics (e.g., Delivery Issues, Customer Support, UX/UI, etc.).
- **Interactive Visualizations**: Includes:
  - Sentiment distribution over feedback.
  - Topic distribution and analysis.
  - Heatmap to show the correlation between sentiment and topic.
- **File Upload**: Upload a CSV or text file with customer feedback for processing.
- **Download Processed Data**: After analysis, you can download a summary CSV of the processed feedback data.

---

## 💻 **How to Run the Project Locally**

To get started with the **Feedback2Action-AI** dashboard, follow these steps:

### 1. **Clone the Repository**
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/Anaghaank/Feedback2Action-AI.git
```

### 2. **Install Dependencies**
Ensure you have Python 3.x installed on your machine. Then, create a virtual environment and install the required libraries:

```bash
cd feedback2action-ai
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scriptsctivate     # For Windows
pip install -r requirements.txt
```

### 3. **Run the Streamlit Dashboard**
Once the dependencies are installed, you can run the dashboard using the command below:

```bash
streamlit run app/dashboard.py
```

The Streamlit app will open in your browser, and you'll be able to upload your customer feedback file for analysis.

---

## 📊 **How to Use the Dashboard**

1. **Upload your feedback file**: Click the "Upload your feedback file" button to upload a CSV or text file that contains customer feedback. Ensure the file has a column named `text`, which holds the feedback text.
2. **View data sample**: Once the file is uploaded, a sample of the data will be displayed.
3. **Sentiment & Topic Analysis**: After the file is processed, the dashboard will show the sentiment and topic analysis results for each piece of feedback.
4. **Interactive Filters**: You can filter the visualizations based on:
   - Sentiment type (Positive, Neutral, Negative).
   - Specific topics like Delivery Issues, Customer Support, etc.
5. **Download Processed Data**: After analyzing the feedback, you can download a summary CSV containing the processed data with sentiment and topic classifications.

---

## 🔧 **Technologies Used**

- **Python 3.x**: The core language for data processing and analysis.
- **Streamlit**: For building the interactive dashboard.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For machine learning tasks, including sentiment analysis (if customized).
- **Seaborn & Matplotlib**: For visualizations like bar charts, heatmaps, and more.
- **Hugging Face's Transformers**: For NLP tasks such as sentiment analysis.

---

## 🛠️ **Development**

To contribute to this project or modify it, follow these steps:

### 1. **Clone the repository**
Clone this repository to your local development environment.
```bash
git clone https://github.com/Anaghaank/Feedback2Action-AI.git
```

### 2. **Install development dependencies**
Install the required packages as described above, or in case of any updates, run:
```bash
pip install -r requirements.txt
```

### 3. **Contributing**
Feel free to open issues or submit pull requests for any improvements. Contributions are welcome!

---

## 💡 **Future Enhancements**

- **Advanced Topic Modeling**: Incorporate more advanced NLP techniques like LDA or BERT for better topic classification.
- **Multi-language Support**: Add functionality to support customer feedback in multiple languages.
- **Real-time Feedback Processing**: Implement real-time feedback processing for businesses with large incoming data streams.

---

## 👨‍💻 **About the Developer**

This project was created by Anagha Ankolekar, a passionate developer working on AI and NLP-driven applications. If you have any questions or suggestions, feel free to reach out or open an issue on the repository.

---

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Conclusion

This project provides a simple yet powerful way to analyze and gain insights from customer feedback using AI. It aims to streamline the process of analyzing sentiment and categorizing feedback into relevant topics, making it easier for businesses to take actionable steps based on customer input.
