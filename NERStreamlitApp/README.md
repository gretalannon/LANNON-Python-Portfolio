## NER Streamlit App

The purpose of this app is to allow users to utilize the named entity recognition (NER) features of natural language processing to sort through the various components within their email compositions. The project uses SpaCy, a rule-based Python library which uses a statistical model and token-based approach for natural language processing.

## Instructions for Use:

App can be accessed through web link to try out features!
To view alongside code, clone repository and use streamlit run command in the terminal to look at app through local host.
Be sure to pip install pandas, spacy, and streamlit.

## App Features:

Using this app, users are able to enter in text and assign custom labels to it. These labels will then be highlighted in their email text below, giving a clear visualization of the composition of the email. The model comes built in with many labels by default through SpaCy, in addition to patterns for TASK labels. The app also assigns a conciseness score to the email based on it's ratio of tokens labelled ADJ or ADV to the other tokens.

## References  

- The Real Python Podcast: Ep 232 Exploring Modern Sentiment Analysis Approaches in Python  
- [EntityRuler Guide](https://spacy.io/api/entityruler)
