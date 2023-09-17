# MovieSage - Movie recommendation engine
## Introduction
This is the repository for "MovieSage", a personalized, prompt-based movie recommandation engine. This was our final 10-days project in the JEDHA Data Science Fullstack bootcamp.

The purpose of our work is to offer an alternative to content-based or user-base recommendation services. MovieSage allows you to describe in details the type of movie you would like to watch, and add somme optional filtering options, in order to obtain a list of potential matches to your request.

Here is a demo video of our app :

https://github.com/SW-Perse/MovieSage/assets/136578812/63138f6c-3c2f-428e-b4bd-333d48ccb079

## Data
Our app currently uses the "Top 10000 popular Movies TMDB" from Kaggle : https://www.kaggle.com/datasets/ursmaheshj/top-10000-popular-movies-tmdb-05-2023

The "EDA" section of this repository explores this dataset in further details.

## Model
MovieSage uses SentenceTransformers' 'all-mpnet-base-v2' for synopsis and user prompt embedding. Documentation on how to use this model can be found here : https://www.sbert.net/

## Setup
Our app can be used locally only, due to volume limitations in free deployment options.

The code for our User Interface (UI) can be found in the "UI" section of this repo and hosted locally using the following command : 
`streamlit run ui.py`

The code for our API can be found in the "API" section of this repo and hosted locally using the following command :
`python api.py`

Access to our database is IP-restricted and requires authorisation upon request. Feel free to reach out if you need access to try out our app!

## Final words
We appreciate any feedback on our code and recommendation system to continue improving our app :)
