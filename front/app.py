import streamlit as st
import requests
from filters import genres, ratings, release_date

st.title("Movie Recommendation")

user_prompt= st.text_input("Enter prompt: ", placeholder="A rogue space explorer plans an intergalactic heist")

st.subheader("Genre")
genre_options = st.multiselect("Select genres:", genres, placeholder="")

st.subheader("Ratings")
rating_options = st.selectbox("Select minimum rating:", ratings, placeholder="")

st.subheader("Release date")
release_date_options = st.selectbox("Select a release date:", release_date, placeholder="")

prompt_button = st.button("Submit", key="prompt")

if prompt_button:
        print(genre_options)
        response = requests.get(f"http://localhost:8000/recommendations", params={"user_prompt": user_prompt,
                                                                                  "rating": rating_options,
                                                                                  "release_date": release_date_options,
                                                                                  "genres": genre_options})
        data = response.json()
        st.write("API Response:")
        st.json(data)