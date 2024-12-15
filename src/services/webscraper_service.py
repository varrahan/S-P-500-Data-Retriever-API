import requests
from bs4 import BeautifulSoup
from requests import Response
from typing import Self
from src.utils.env_utils import env_utils
from src.utils.logger_config import logger


class WebscraperService(): 
    __web_url: str = ''
    
    def __init__(self: Self) -> None:
        self.__web_url = env_utils['WEB_URL']

    def pull_table_data(self: Self) -> list[list[str]]:
        try: 
            data: list[list[str]] = []
            page: int = 1
            while True:
                # Fetch the webpage
                url: str = f'{self.__web_url}?p={page}'
                response: Response = requests.get(url)
                soup: BeautifulSoup = BeautifulSoup(response.content, "html.parser")
                # Find the table on the webpage
                table: str = soup.find("table", {"class": "table"})
                # Stop if page does not have a table
                if not table:
                    break
                # Extract rows from the table
                for row in table.find_all("tr")[1:]:
                    cols: list[str] = row.find_all("td")
                    row_data: list[str] = []
                    for col in cols:
                        # Extract each cell's data, handling spans and line breaks
                        cell_data: list[str] = self.extract_cell_data(col)
                        # Check if there were multiple values in a cell without being inside a span
                        if '\n' in cell_data[0]:
                            cell_data = self.split_cell_on_newline(cell_data)
                        row_data.extend(cell_data)
                    if row_data and row_data[0] != '':
                        data.append(row_data)
                page += 1
        except Exception as ex:
            logger.exception(f'Error has occured with the pull_table_data function in the WebscraperService: {ex}')
        return data
    
    def split_cell_on_newline(self: Self, input_cell: list[str]) -> list[str]:
        # Split single element cell where string has a newline char
        cell: list[str] = input_cell[0].split('\n')
        return cell

    def extract_cell_data(self: Self, cell: str) -> list[str]:
        spans: list[str] = cell.find_all("span")
        if spans:
            # If spans exist append all values in span to an array
            return [span.text.strip() for span in spans]
        # If spans do not exist return array with single string element
        return [cell.text.strip()] 
            