from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')

env_utils: dict[str,str] = {
    'DATABASE_NAME': getenv('DATABASE_NAME'),
    'WEB_URL': getenv('WEB_URL'),
    'CONTAINER_PORT': int(getenv('CONTAINER_PORT')),
    'MONGO_PORT': int(getenv('MONGO_PORT')),
    'MONGO_PWD': getenv('MONGO_PWD'),
    'MONGO_USER': getenv('MONGO_USER'),
    'MONGO_HOST': getenv('MONGO_HOST')
}