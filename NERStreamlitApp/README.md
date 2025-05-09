# Email Style & Sentiment Analyzer

## Project Overview
The purpose of this app is to allow users to utilize the named entity recognition (NER) features of natural language processing to sort through the various components within their email compositions. The project uses SpaCy, a rule-based Python library which uses a statistical model and token-based approach for natural language processing.

## Instructions for Use

### Requirements

Ensure the following Python libraries are installed:

- `pandas`  
- `streamlit`  
- `matplotlib`  
- `numpy`
- `seaborn`

### To run the app locally...

1. Clone the repository:  
   `git clone https://github.com/gretalannon/LANNON-Python-Portfolio/NERStreamlitApp.git`

2. Navigate to the app directory and run:  
   `streamlit run main.py`

### Or, use web link...

[Click Here!](https://nerprojectgretalannon.streamlit.app/)

## App Features:

Using this app, users are able to enter in text and assign custom labels to it. These labels will then be highlighted in their email text below, giving a clear visualization of the composition of the email. The model comes built in with many labels by default through SpaCy, in addition to patterns for TASK labels. The app also assigns a conciseness score to the email based on it's ratio of tokens labelled ADJ or ADV to the other tokens.

## References  

- The Real Python Podcast: Ep 232 Exploring Modern Sentiment Analysis Approaches in Python  
- [EntityRuler Guide](https://spacy.io/api/entityruler)
