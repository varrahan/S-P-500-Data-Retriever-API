from flask import Flask
from src.routers.router import setup_routes
from src.utils.logger_config import logger_config
from src.utils.env_utils import env_utils

app: Flask = Flask(__name__)

setup_routes(app)
logger_config()

if __name__ == '__main__':
    app.run(debug=True, port=env_utils['CONTAINER_PORT'])
    