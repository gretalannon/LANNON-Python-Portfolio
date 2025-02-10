import streamlit as st
import pandas as pd

# title/description
st.title("Baby Names of 2023")
st.write("2023 welcomed millions of babies into our world. The burning question is, of course, what are these now-two-year-olds called? This app allows you to sort through the most popular names for boys and girls in 2023.")

# connecting the dataset
df = pd.read_csv("data/girl_boy_names_2023.csv")


# Heading for interaction one: popular name slider
st.markdown("# Most Popular 🎉")

# Setting up slider to select up to 20 of the top boy/girl names
number_of_names = st.slider("How many of the top names would you like to see?", 1, 20, 1)
st.write(f"Here are the top {number_of_names} names:")

for i in range(number_of_names):
    rank = df["Rank"][i]
    boy_name = df["Boy Name"][i]
    girl_name = df["Girl Name"][i]
    st.markdown(f"{boy_name}, #{rank} (boy)")
    st.markdown(f"{girl_name}, #{rank} (girl)")

# Setting up interaction 2: sorting names by letter
st.markdown("# Sort by Letter...")
# Select box, includes full alphabet of letters to choose from
letter = st.selectbox("Names starting with...", list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
# setting up variables to choose names that start with letter (.startswith function)
filtered_boy_names = df[df["Boy Name"].str.startswith(letter)]
filtered_girl_names = df[df["Girl Name"].str.startswith(letter)]

st.write(f"Boy names starting with {letter}:")
for name in filtered_boy_names["Boy Name"]:
    st.write(name)

st.write(f"Girl names starting with {letter}:")
for name in filtered_girl_names["Girl Name"]:
    st.write(name)

# Setting up interaction 3: is your name in the top 1000?
st.markdown("# Did your name make the 2023 top 1000 list?")
name_of_user = st.text_input("Your name")
# if/else function to see if text entry by user comes up empty or not in dataset
if name_of_user:
    user_boy = df[df["Boy Name"] == name_of_user]
    user_girl = df[df["Girl Name"] == name_of_user]

    if user_boy.empty == False or user_girl.empty == False:
        st.write(f"Yes!! {name_of_user} was a top 1000 baby name in 2023!")
    else:
        st.write(f"{name_of_user} was not a top 1000 name in 2023. Perhaps it's gone out of style...")