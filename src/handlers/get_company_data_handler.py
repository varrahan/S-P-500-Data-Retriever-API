from flask import jsonify, Response, Request
from typing import Any
from src.services.database_service import DatabaseService
from src.utils.logger_config import logger

def get_company_data_handler(request: Request) -> Response:
    logger.info('Request to get financial data from selected company in database has been made')
    response: dict[str, Any] = {
        'status': 200
    }
    results: list[dict[str,Any]]
    try:
        database_service: DatabaseService = DatabaseService()
        company: str = request.args.get('company')
        logger.info(company)
        if not company:
            response['status'] = 400
            response['errMessage'] = 'No company has been selected'
            return jsonify(response), response['status']
        results = database_service.get_collection_data(company)
        response['results'] = results
    except Exception as ex:
        response['status'] = 500
        response['errMessage'] = f'An error has occured: {ex}'
        logger.exception(f'An error has occured with the get_company_data_handler: {ex}')
    return jsonify(response), response['status']
