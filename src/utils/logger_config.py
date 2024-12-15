from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from loguru import logger
from datetime import datetime
from typing import Any
from src.utils.db_config import DATABASE
from sys import stdout

log_collection: Collection = DATABASE['logs']

def mongo_sink(message: Any) -> None:
    log_record: dict[str,Any] = message.record
    # Create entries which will store all log data in collection
    entry: dict[str,Any] = {
        "time": datetime.strptime(log_record["time"].strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"),
        "level": log_record["level"].name,
        "message": log_record["message"],
        "function": log_record["function"],
        "line": log_record["line"],
        "module": log_record["module"],
        "file": log_record["file"].name,     
    }
    log_collection.insert_one(entry)

def logger_config() -> Any:
    logger.remove()
    logger.add(
        stdout,
        format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}',
        level='DEBUG',
        colorize=True,
    )
    logger.add(mongo_sink, level='DEBUG')
    return logger
    
logger_config()
    
    
