import uvicorn
from fastapi import FastAPI, Query
from typing import List

from functions import user_query_embedding_all, query_database, recommendations_all

app = FastAPI()

@app.get("/")
async def index():

    message = "Hello world! This `/` is the most simple and default endpoint. If you want to learn more, check out documentation of the api at `/docs`"

    return message

@app.get("/recommendations")
async def get_recommendations(user_prompt: str, rating: int, release_date: int, nb_recos:int, genres: List[str] = Query(None)):
    titles, synopsis, embedding_all = query_database(genres, rating, release_date)
    query_all = user_query_embedding_all(user_prompt)
    recos_all = recommendations_all(query_all, titles, synopsis, embedding_all, nb_recos)
    return recos_all

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)