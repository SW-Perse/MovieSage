from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

USER_NAME = config("USER_NAME")
DB_PASSWORD = config("DB_PASSWORD")
HOST_NAME = config("HOST_NAME")
DB_PORT = config("DB_PORT")
DB_NAME = config("DB_NAME")

DATABASE_URL = f"postgresql://{USER_NAME}:{DB_PASSWORD}@{HOST_NAME}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)