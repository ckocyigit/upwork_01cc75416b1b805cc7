import requests
from bs4 import BeautifulSoup
import json

class MaricopaJCCH:

    def __init__(self, base_url):
        self.base_url = base_url
        self.mainTableName = "MainContent_CaseSearchResultsGridView"

    def search(self, lastName = "", firstName = "", DOB = ""):

        query_params = {
            "lastName": lastName,
            "FirstName": firstName,
            "DOB": DOB
        }

        response = requests.get(self.base_url, params=query_params)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': self.mainTableName})
        if table is not None:
            data = []

            for row in table.find_all('tr')[1:]:
                cells = row.find_all('td')

                data.append({cells[0].text.strip(): cells[1].text.strip().replace('\r', '').replace('\n', '').replace('\t', '')})

            return json.dumps(data)
        else:
            print("No results.")