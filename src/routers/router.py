from flask import Blueprint, Flask, Response, jsonify
from src.handlers.store_data_handler import store_data_handler

app_router: Blueprint = Blueprint('router', __name__)

@app_router.route('/store', methods=['POST'])
def store_route() -> Response:
    return store_data_handler()

def setup_routes(app: Flask) -> None:
    app.register_blueprint(app_router)