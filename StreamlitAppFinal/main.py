import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Bring in the data
df = pd.read_csv("Data/sample_product_reviews.csv")

#Title
st.title("Design Research Review Sentiment Analyzer")

data_source = st.radio(
    "Choose your data source:",
    ("Use sample data", "Upload my own CSV file")
)

# Load the dataset based on user choice
df = None

if data_source == "Use sample data":
        df = pd.read_csv("Data/sample_product_reviews.csv")
        st.success("Sample data loaded successfully!")

elif data_source == "Upload my own CSV file":
    uploaded_file = st.file_uploader("Upload your CSV file", type = ["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("Your data uploaded successfully!")
        except Exception as e:
            st.error(f"Error loading you file: {e}")
    else:
        st.info("Upload your CSV file!")

analyzer = SentimentIntensityAnalyzer()
def vader_sentiment_analyzer(review):
    # Analyze the sentiment of a sample text
    vader_scores = analyzer.polarity_scores(review)

    # Interpreting the compound score
    compound_score = vader_scores["compound"]
    if compound_score >= 0.05:
        return "positive"
    elif compound_score <= -0.05:
        return "negative"
    else:
        return "neutral"
df["vader_sent"] = df["review"].apply(vader_sentiment_analyzer)

st.write("Sentiment Analysis Preview:")
st.dataframe(df[["review", "vader_sent"]].head())


#-------------------------------------------------------------------------
# Word Cloud to show the most common words in positive reviews, and the most common words in negative reviews
st.markdown("### Common Themes")
st.write("What stuck out to your users? See what the commons themes and emotions among your users were, organized by positive and negative reviews.")

positive_reviews = df[df["vader_sent"] == "positive"]["review"]
negative_reviews = df[df["vader_sent"] == "negative"]["review"]

# Use the .join function to merge all the reviews together (by sentiment)
positive_reviews_text = " ".join(positive_reviews)
negative_reviews_text = " ".join(negative_reviews)

# Positive reviews:
wordcloud_pos = WordCloud(
    width=800, 
    height=400,  
    background_color="white",
    colormap="Greens"
).generate(positive_reviews_text)

# Negative reviews word cloud:
wordcloud_neg = WordCloud(
    width = 800, 
    height = 400, 
    background_color="white",
    colormap = "Reds"
).generate(negative_reviews_text)

# Plot setup to fit layout
fig, axes = plt.subplots(1, 2, figsize = (16, 8))

# Show the word clouds using .imshow.
axes[0].imshow(wordcloud_pos)
axes[0].axis("off")
axes[0].set_title("Most Common Words in Positive Reviews")

# repeat with negative cloud
axes[1].imshow(wordcloud_neg)
axes[1].axis("off")
axes[1].set_title("Most Common Words in Negative Reviews")

#figure appear in the streamlit app
st.pyplot(fig)


#-------------------------------------------------------------------------
# Bar plot to show which regions were most positive in their reviews about the product
st.markdown("### Demographics")
st.write("Now let's take a closer look at demographics. Which parts of the market are responding well to your product?")

#Select box to choose which demographic
group_col = st.selectbox("Group sentiment by:", options = ["region", "gender"])

#grouping columns
sentiment_counts = df.groupby([group_col, "vader_sent"]).size().unstack(fill_value = 0)

# Percentage calculation to account for different count numbers
sentiment_counts["percent_positive"] = 100 * sentiment_counts["positive"] / sentiment_counts.sum(axis = 1)

# sorting so that most positive is at the top not the bottom
sentiment_sorted = sentiment_counts.sort_values(by = "percent_positive", ascending = False)

# Setting up the visualization so it has proper layout
fig, ax = plt.subplots(figsize = (10, 6))
sentiment_sorted['percent_positive'].plot(kind = "barh", ax = ax, color = "green")
ax.set_title(f"% Positive Sentiment by {group_col.capitalize()}")
ax.set_xlabel("Percent Positive")
ax.set_ylabel(group_col.capitalize())
ax.invert_yaxis()

#Display it
st.pyplot(fig)

#-------------------------------------------------------------------------
st.markdown("### Overall Sentiment Breakdown")
# General percentages of positive vs. negative

total_reviews = len(df)
positive_count = (df["vader_sent"] == "positive").sum()
negative_count = (df["vader_sent"] == "negative").sum()

# Use function to find percentages using length and counts of positive vs negative
positive_percent = (positive_count / total_reviews) * 100
negative_percent = (negative_count / total_reviews) * 100

# Print the Results
st.write(f"**Positive Reviews:** {positive_count} ({positive_percent}%)")
st.write(f"**Negative Reviews:** {negative_count} ({negative_percent}%)")
