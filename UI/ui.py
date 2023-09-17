import streamlit as st
import requests
from filters import genres, ratings, release_date
from PIL import Image
import time

# Set page config
st.set_page_config(
    page_title="MovieSage",
    page_icon="🎬",
    layout="wide"
)

# Apply the custom CSS
custom_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #4d4855;
    background-image: linear-gradient(to left, #434343 0%, black 100%);
    opacity : 1;
    color: white; /* Set text color to white */
}
[data-testid="stHeader"] {
    background-color : rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Header
image = Image.open("Logo_MovieSage_Pour_fond_Noir.png")
st.image(image, width = 500)

# Title
st.markdown("<h2 style='text-align: left; color: #C0C0C0;'>Creating memories, one cinematic journey at a time</h2>", unsafe_allow_html=True)

# Short Description
st.markdown("What will you be watching today?  \n"
            "MovieSage is a personalized, content-based movie recommandation engine")

# Explanation/Example
st.markdown("Use the prompt space to describe the movie you want. Be as specific and detailed as you wish!")

# User Input
user_prompt= st.text_input("Describe the movie of your dreams! For example : ", placeholder="A rogue space explorer plans an intergalactic heist")

# Select Boxes
st.subheader("Choose optional settings to filter results :")
genre_options = st.multiselect("Select genres:", genres, placeholder="")

rating_options = st.selectbox("Minimum rating:", ratings, index=0, placeholder="")

release_date_options = st.selectbox("Released after:", release_date, index=0, placeholder="")

st.write("")
st.write("How many recommendations would you like?")
nb_recos = st.number_input("Enter a number", value=1, min_value=1)

# Submit Button
prompt_button = st.button("Submit", key="prompt")

if prompt_button:
   with st.status("Looking for your personalized recommendations...", expanded=True) as status:
      response = requests.get(f"http://localhost:8000/recommendations", params={"user_prompt": user_prompt,
                                                                                  "rating": rating_options,
                                                                                  "release_date": release_date_options,
                                                                                  "genres": genre_options,
                                                                                   "nb_recos": nb_recos})
      st.write("Searching our database...")
      time.sleep(1)
      st.write("Matching your request...")
      time.sleep(1)
      st.write("Downloading results...")
      time.sleep(1)
      status.update(label="Done!", state="complete", expanded=False)
      
   print(genre_options, rating_options, release_date_options)
         
   st.write("Here are your personalized recommandations!")
   recos = response.json()
   for i in range(len(recos)): 
     st.write("- " , recos[i]["rank"] , " : " , recos[i]["title"] , "\n")#, recos[0]["summary"])

# Sidebar
st.sidebar.header("The team")
st.sidebar.write("Made with ♥️ and 🤖")
st.sidebar.write("by Charlotte, Laurie, Sophie & Victor")
st.sidebar.write("@JEDHA")