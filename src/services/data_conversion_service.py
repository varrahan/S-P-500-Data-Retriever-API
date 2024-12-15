from typing import Self, Any
from src.utils.logger_config import logger

class DataConversionService():
    def convert_to_json(self: Self, table_rows: list[list[str]]) -> list[dict[str,Any]]:
        try:
            json_list: list[dict[str, Any]] = []
            for row in table_rows:
                # Convert row data for each company at time = timestamp into the document format that will be stored in MongoDB
                # Convert all pprice strings into floats
                data: dict[str,str] = {
                    'companyName': row[0],
                    'timestamp': row[8],
                    'previousClose': float(row[2].replace(',','')),
                    'low': float(row[3].replace(',','')),
                    'high': float(row[4].replace(',','')),
                    'marketValue': {
                        'price': float(row[1].replace(',','')),
                        'valueChange': float(row[5].replace(',','')),
                        'percentageChange': row[6]
                    },
                    'longTermPerformance': {
                        'dollarAmount': {
                            'threeMonth': float(row[9].replace(',','')),
                            'sizMonth': float(row[11].replace(',','')),
                            'oneYear': float(row[13].replace(',',''))
                        },
                        'percentage': {
                            'threeMonth': row[10],
                            'sixMonth': row[12],
                            'oneYear': row[14]
                        },
                    },
                }
                json_list.append(data)
        except Exception as ex:
            logger.exception(f'Error has occured with the convert_to_json function in the DataConversionService: {ex}')
        return json_list