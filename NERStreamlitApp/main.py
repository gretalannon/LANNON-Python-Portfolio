# import necessities
import streamlit as st
import pandas as pd

#load in the spaCy models to determine spaCy was downloaded correctly
# import displacy for highlighted text render
import spacy 
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

# title/description
st.title("Email Analyzer")
st.write("Emails are the foundation of digital communication in the workplace, at school, or even between friends. This app uses named entity recognition (NER) to allow you to analyze the parts that make up your email. Finally, the app assigns a conciseness score based on the ratio of filler words!")

# Input space for user to enter their email draft, or use provided example
user_email = st.text_input("Your Email Composition (not address!)")

# default recipe/provided example
example_email = "Hi Jordan, I hope you're having a great morning! I just wanted to quickly follow up on the status of the Q2 budget report. I know things have been a bit hectic lately, but if you could share the latest draft by Wednesday afternoon, that would be amazing. Also, I had a quick thought about the upcoming client presentation — maybe we could brainstorm a few creative visuals during our team check-in tomorrow? Thanks so much for all your hard work lately. Really appreciate it! Best, Taylor"

# Use user input if it has something written there, otherwise use example email.
doc = user_email if user_email != "" else example_email


# CUSTOM LABEL PATTERNS: BUILT IN & USER CREATED

# Built in patterns...
entity_patterns = [
    {"label": "TASK", "pattern": "follow up"},
    {"label": "TASK", "pattern": "check-in"},
    {"label": "TASK", "pattern": "brainstorm"},
    {"label": "TASK", "pattern": "meeting"},
    {"label": "TASK", "pattern": "project"},
    {"label": "TASK", "pattern": "deadline"},
    {"label": "TASK", "pattern": "task"},
    {"label": "TASK", "pattern": "report"},
    {"label": "TASK", "pattern": "draft"}
]

# Check if the "ner" pipe exists. If it does, add the EntityRuler before it.
if "ner" in nlp.pipe_names:
    # If entity_ruler already exists, simply add patterns to it.
    try:
        ruler = nlp.get_pipe("entity_ruler")
    except Exception:
        ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.add_patterns(entity_patterns)
else:
    # If the NER component does not exist, add both the EntityRuler and the NER component.
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(entity_patterns)
    ner = nlp.add_pipe("ner")

# User made patterns...
st.subheader("Create Your Own Labels!")

# making input boxes for user to enter their text and labels
custom_phrase = st.text_input("Text")
custom_label = st.text_input("Custom Label")

#adding those parameters to the ruler
if st.button("Add Custom Rule") and custom_phrase and custom_label:
    pattern = {"label": custom_label.upper(), "pattern": custom_phrase}
    ruler.add_patterns([pattern])

# NLP pipeline
doc = nlp(doc)

# Table of entities and their labels
st.subheader("Entities:")
#List to collect entity data
entities_data = []

# Extracted entities and their labels...
for ent in doc.ents:
    entities_data.append({
        "text": ent.text,
        "label": ent.label_
    })
# set it up as a dataframe so it's formatted nicely in app
ent_df = pd.DataFrame(entities_data)
st.write(ent_df)

# Render displaCy as HTML since jupyter method used in google colab doesn't work in VS code
html = displacy.render(doc, style="ent")
st.markdown(html, unsafe_allow_html=True)


# Final Analysis method: conciseness score
st.subheader("Conciseness")
st.write("Based on your usage of adjectives and adverbs, the app assigns a conciseness score to your email. The scores range from 0 (most concise) to 1 (least concise).")

# Conciseness Score =Ratio of adjectives and adverbs to non-adjectives
# count up number of tokens that are filler (adj or adv) and compare to total tokens excluding punctuation. Len gives the count
adjadv_tokens = [token.text for token in doc if token.pos_ == "ADJ" or token.pos_ == "ADV"]
total_tokens = [token for token in doc if token.is_punct == False] #don't factor punctuation into ratio
conciseness_score = len(adjadv_tokens) / len(total_tokens) if len(total_tokens) > 0 else 0
# Display the conciseness score
st.write("Your Conciseness Score: ", conciseness_score)