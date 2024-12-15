from typing import Self, Any
from pymongo.collection import Collection
from pymongo import MongoClient, database
from src.utils.db_config import DATABASE
from src.utils.logger_config import logger


class DatabaseService():
    def add_to_collection(self: Self, document: dict[str,str]) -> bool:
        try:
            status: bool = False
            company: str = document['companyName']
            collection: Collection = DATABASE[company]
            # Check if collection for company name exists in mongodb
            if collection is not None:
                # Insert document into collection
                result: Any = collection.insert_one(document)
                if result:
                    status = True
        except Exception as ex:
            logger.exception(f'Error has occured with the add_to_collection function in the DatabaseService: {ex}')
        return status
    
    def get_collection_data(self: Self, company: str) -> list[dict[str,Any]]:
        try:
            documents: list[dict[str,Any]] = []
            collection: Collection = DATABASE[company]
            # Iterate and return all documents from the collection as a list of JSONs
            for document in collection.find():
                documents.append(document)
        except Exception as ex:
            logger.exception(f'Error has occured with the get_collection_data function in the DataConversionService: {ex}')
        return documents
            
        
        
        
    
    