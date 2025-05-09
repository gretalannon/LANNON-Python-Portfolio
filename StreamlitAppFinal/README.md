# Design Research Review Sentiment Analyzer

## Project Overview
My final streamlit app for the Elements of Computing II course examines text review data to determine general trends in user feedback for a product.

## Instructions for Use

### Requirements

Ensure the following Python libraries are installed:

- `pandas`  
- `streamlit`  
- `matplotlib`  
- `numpy`
- `nltk`
- `seaborn`
- `wordcloud`

### To run the app locally...

1. Clone the repository:  
   `git clone https://github.com/gretalannon/LANNON-Python-Portfolio/StreamlitAppFinal.git`

2. Navigate to the app directory and run:  
   `streamlit run main.py`

### Or, use web link...

[Click Here!](https://designresearchsentimentanalyzer.streamlit.app/)

## App Features

- User uploads CSV file of their user reviews for a product. This file can come from a google form!
- App will give you a score for overall sentiment--the percentage of positive to negative reviews
- You can sort reviews by demographic categories in order to see which users reviewed the product more favorably.
- Word cloud shows words that came up most in the reviews. If something was a common point of interest in the reviews, good or bad, it will show up in the word clouds.

## References & Resources:
- [Streamlit Official Documentation](https://docs.streamlit.io/)
