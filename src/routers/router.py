from flask import Blueprint, Flask, Response, request
from src.handlers.store_data_handler import store_data_handler
from src.handlers.get_company_data_handler import get_company_data_handler

app_router: Blueprint = Blueprint('router', __name__)

@app_router.route('/store', methods=['POST'])
def store_route() -> Response:
    return store_data_handler()

@app_router.route('/getData', methods=['GET'])
def get__data_route() -> Response:
    return get_company_data_handler(request)

def setup_routes(app: Flask) -> None:
    app.register_blueprint(app_router)