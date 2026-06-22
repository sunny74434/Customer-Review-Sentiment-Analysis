     
import streamlit as st
import pandas as pd
from sentiment_analyzer import analyze_sentiment


st.title("Customer Review Sentiment Analyzer")

option = st.sidebar.selectbox(
    "Choose Option",
    ["Single Review Analysis","Upload CSV Reviews"]
)

if option == "Single Review Analysis":
    
    review = st.text_area("Enter Customer Review")
    
    if st.button("Analyze Sentiment"):
        
        if not review.strip():                       # ✅ Added: empty input check
            st.warning("Please enter a review first.")
        else:
            result = analyze_sentiment(review)

        
        
        st.subheader("Sentiment Result")
        
        if result == "Positive":
            st.success("Positive Review")
        
        elif result == "Negative":
            st.error("Negative Review")
        else:
            st.warning("Neutral Review")

if option == "Upload CSV Reviews":
    
    file = st.file_uploader("Upload CSV file")
    
    if file:
        
        df = pd.read_csv(file)
        review_column = st.selectbox("Select the text column for analysis:",df.columns)
        
        sentiments = []
        
        for review in df[review_column]:
            sentiment = analyze_sentiment(review)
            sentiments.append(sentiment)
            
        df["Sentiment"] = sentiments
        
        st.write(df)
        
        st.bar_chart(df["Sentiment"].value_counts())            