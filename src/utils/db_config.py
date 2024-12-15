from pymongo import MongoClient
from pymongo.database import Database
from src.utils.env_utils import env_utils

def connect_log_db() -> Database:
    # Connect to log collection in database 
    host: str = env_utils['MONGO_HOST']
    port: int = env_utils['MONGO_PORT']
    user: str = env_utils['MONGO_USER']
    pwd: str =  env_utils['MONGO_PWD']
    database: str = env_utils['DATABASE_NAME']
    
    connection_string: str = f'mongodb://{user}:{pwd}@{host}:{port}/'

    client: MongoClient = MongoClient(connection_string)
    
    db: Database = client.get_database(database)
    return db

DATABASE = connect_log_db()