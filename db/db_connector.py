import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

database = os.getenv('POSTGRES_DATABASE'),
user = os.getenv('POSTGRES_USER'),
password = os.getenv('POSTGRES_PASSWORD'),
host = "localhost",
port = os.getenv('POSTGRES_PORT')

engine = create_engine(
    "postgresql+psycopg2://""postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}".format(
        db_username=user,
        db_password=password,
        db_host=host,
        db_port=port,
        db_name=database
    ),
    echo=True
)


def create_connection():
    return engine.connect()
