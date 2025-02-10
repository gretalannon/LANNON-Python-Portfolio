import streamlit as st
import pandas as pd

st.title("Baby Names of 2023")
st.write("2023 welcomed millions of babies into our world. The burning question is, of course, what are these now-two-year-olds called? This app allows you to sort through the most popular names for boys and girls in 2023.")

df = pd.read_csv("data/girl_boy_names_2023.csv")

st.markdown("# Most Popular 🎉")

number_of_names = st.slider("How many of the top names would you like to see?", 1, 20, 1)
st.write(f"Here are the top {number_of_names} names:")

for i in range(number_of_names):
    rank = df["Rank"][i]
    boy_name = df["Boy Name"][i]
    girl_name = df["Girl Name"][i]
    st.markdown(f"{boy_name}, #{rank} (boy)")
    st.markdown(f"{girl_name}, #{rank} (girl)")

df = pd.read_csv("data/girl_boy_names_2023.csv")

st.markdown("# Sort by Letter...")
letter = st.selectbox("Names starting with...", list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
filtered_boy_names = df[df["Boy Name"].str.startswith(letter)]
filtered_girl_names = df[df["Girl Name"].str.startswith(letter)]

st.write(f"Boy names starting with {letter}:")
for name in filtered_boy_names["Boy Name"]:
    st.write(name)

st.write(f"Girl names starting with {letter}:")
for name in filtered_girl_names["Girl Name"]:
    st.write(name)

st.markdown("# Did your name make the 2023 top 1000 list?")
name_of_user = st.text_input("Your name")
if name_of_user:
    user_boy = df[df["Boy Name"] == name_of_user]
    user_girl = df[df["Girl Name"] == name_of_user]

    if user_boy.empty == False or user_girl.empty == False:
        st.write(f"Yes!! {name_of_user} was a top 1000 baby name in 2023!")
    else:
        st.write(f"{name_of_user} was not a top 1000 name in 2023. Perhaps it's gone out of style...")