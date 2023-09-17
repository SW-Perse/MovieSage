from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    genres = Column(ARRAY(String))
    vote_average = Column(Float)
    overview = Column(String)
    runtime = Column(Float)
    tagline	= Column(String)
    text_description = Column(String)

class Embedding_all(Base):
    __tablename__ = "embedding_all"

    movie_id = Column(Integer, primary_key=True)
    embedding = Column(ARRAY(Float))

class Embedding_multi(Base):
    __tablename__ = "embedding_multi"

    movie_id = Column(Integer, primary_key=True)
    embedding = Column(ARRAY(Float))

class Embedding_marco(Base):
    __tablename__ = "embedding_marco"

    movie_id = Column(Integer, primary_key=True)
    embedding = Column(ARRAY(Float))
