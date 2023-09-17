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
    if genres is None:
        query = session.query(Movies.id, Movies.title, Movies.overview, Embedding_all.embedding)\
                 .join(Embedding_all, Embedding_all.movie_id == Movies.id)\
                 .filter(extract('year',Movies.release_date) >= release_date, Movies.vote_average >= rating)\
                 .all()
    else:
        query = session.query(Movies.id, Movies.title, Movies.overview, Embedding_all.embedding)\
                  .join(Embedding_all, Embedding_all.movie_id == Movies.id)\
                  .filter(Movies.genres.contains(genres), extract('year',Movies.release_date) >= release_date, Movies.vote_average >= rating)\
                  .all()
    titles = [title for _, title, _, _ in query]
    synopsis = [synopsis for _, _, synopsis, _ in query],
    embeddings = [embedding for _, _, _, embedding in query]
    embedding_array = np.array(embeddings, dtype= "float32")
    print(type(synopsis))
    print(len(synopsis))
    return titles, synopsis, embedding_array

def recommendations_all(query_all, titles, synopsis, embedding_all, nb_recos):
  result = util.semantic_search(query_all, embedding_all, top_k= nb_recos)
  recos_all = []
  if len(titles)==0:
    sorry_msg = "Sorry, we couldn't find any match! Please try again, perhaps with less selective settings?"
    return sorry_msg
  elif len(titles) <= nb_recos:
    for i in range (len(titles)):
      reco_rank = i+1
      title = titles[result[0][i]["corpus_id"]]
      #summary = synopsis[result[0][0][i]["corpus_id"]]
      #score = result[0][i]["score"]
      i_dict = {"rank" : reco_rank, "title" : title}# "summary" : summary}
      recos_all.append(i_dict) 
  else:  
    for i in range (nb_recos):
      reco_rank = i+1
      title = titles[result[0][i]["corpus_id"]]
      #summary = synopsis[result[0][0][i]["corpus_id"]]
      #score = result[0][i]["score"]
      i_dict = {"rank" : reco_rank, "title" : title}# "summary" : summary}
      recos_all.append(i_dict)
  return recos_all 