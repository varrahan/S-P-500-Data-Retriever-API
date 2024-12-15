from flask import jsonify, Response
from typing import Any
from src.services.database_service import DatabaseService
from src.services.data_conversion_service import DataConversionService
from src.services.webscraper_service import WebscraperService
from src.utils.logger_config import logger

def store_data_handler() -> Response:
    logger.info('Request to store financial data in database has been made')
    response: dict[str, Any] = {
        'status': 200
    }
    results: list[dict[str,Any]] = []
    try:
        database_service: DatabaseService = DatabaseService()
        data_converstion_service: DataConversionService = DataConversionService()
        webscraper_service: WebscraperService = WebscraperService()
        
        table_data: list[list[str]] = webscraper_service.pull_table_data()
        jsons: list[dict[str,str]] = data_converstion_service.convert_to_json(table_data)
        for json in jsons:
            status: bool = database_service.add_to_collection(json)
            results.append({
                'companyName': json['companyName'],
                'status': status
            })
            response['results'] = results
    except Exception as ex:
        response['errMessage'] =  f'an error has occured: {ex}'
        response['status'] = 500
        logger.exception(f'Error has occured with the store_data_handler: {ex}')
    return jsonify(response), response['status']
        