import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USER_NAME = os.environ["USER_NAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
HOST_NAME = os.environ["HOST_NAME"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

DATABASE_URL = f"postgresql://{USER_NAME}:{DB_PASSWORD}@{HOST_NAME}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)