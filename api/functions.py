from sqlalchemy import extract
import numpy as np

from sentence_transformers import SentenceTransformer, util

from models import embedder_all
from config import Session
from schemas import Movies, Embedding_all

embedder_all = SentenceTransformer('all-mpnet-base-v2')
embedder_qa = SentenceTransformer('multi-qa-mpnet-base-cos-v1')
embedder_msmarco = SentenceTransformer('msmarco-distilbert-base-v4')

def user_query_embedding_all(user_prompt):
  query_all = embedder_all.encode(user_prompt)
  return query_all

def query_database(genres, rating, release_date):
    session = Session()
    query = session.query(Movies.id, Movies.title, Embedding_all.embedding)\
                 .join(Embedding_all, Embedding_all.movie_id == Movies.id)\
                 .filter(Movies.genres.contains(genres), extract('year',Movies.release_date) >= release_date, Movies.vote_average >= rating)\
                 .all()
    titles = [title for _, title, _ in query]
    embeddings = [embedding for _, _, embedding in query]
    embedding_array = np.array(embeddings, dtype= "float32")
    return titles, embedding_array

def recommendations_all(query_all, titles, embedding_all):
    result = util.semantic_search(query_all, embedding_all, top_k= 10)
    recos_all = []
    for i in range (10):
      reco_rank = i+1
      title = titles[result[0][i]["corpus_id"]]
      score = result[0][i]["score"]
      i_dict = {"rank" : reco_rank, "title" : title, "score" : score}
      recos_all.append(i_dict)
    return recos_all 