import streamlit as st
import requests
from filters import genres, ratings, release_date

st.title("MovieSage")

user_prompt= st.text_input("Enter a prompt: ", placeholder="A rogue space explorer plans an intergalactic heist")

genre_options = st.multiselect("Select genres:", genres, placeholder="")

rating_options = st.selectbox("Select minimum rating:", ratings, placeholder="")

release_date_options = st.selectbox("Select a release date:", release_date, placeholder="")

nb_recos = st.number_input("Number of recommendations", value=1, min_value=1)

prompt_button = st.button("Submit", key="prompt")

if prompt_button:
        response = requests.get(f"http://localhost:8000/recommendations", params={"user_prompt": user_prompt,
                                                                                  "rating": rating_options,
                                                                                  "release_date": release_date_options,
                                                                                  "genres": genre_options,
                                                                                  "nb_recos": nb_recos})
        data = response.json()
        st.write("API Response:")
        st.json(data)