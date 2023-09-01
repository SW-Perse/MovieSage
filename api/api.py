import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from typing import List

from functions import user_query_embedding_all, query_database, recommendations_all

app = FastAPI()

origins = ["http://localhost:3000"]
middleware = [
    Middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
]

app = FastAPI(middleware=middleware)

@app.get("/")
async def index():

    message = "Hello world! This `/` is the most simple and default endpoint. If you want to learn more, check out documentation of the api at `/docs`"

    return message

@app.get("/recommendations")
async def get_recommendations(user_prompt: str, rating: int, release_date: int, genres: List[str] = Query(None)):
    query_all = user_query_embedding_all(user_prompt)
    titles, embedding_all = query_database(genres, rating, release_date)
    recos_all = recommendations_all(query_all, titles, embedding_all)
    return recos_all


@app.get("/items/")
def read_items(q: List[str] = Query(None)):
    return {"q": q}

# @app.get("/prompt")
# async def prompt(rating: int, date: int):
#     session = Session()
#     result = session.query(Movies) \
#                 .filter(extract('year',Movies.release_date) >= date, Movies.vote_average >= rating) \
#                 .with_entities(Movies.title, Movies.id).all()
#     print(result)
#     session.close()
#     return result

# @app.get("/test")
# async def prompt(user_input, rating: int, date: int):
#     session = Session()
#     result = session.query(Movies) \
#                 .filter(extract('year',Movies.release_date) >= date, Movies.vote_average >= rating) \
#                 .with_entities(Movies.title, Movies.id).all()
#     print(result)
#     session.close()
#     return result

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)