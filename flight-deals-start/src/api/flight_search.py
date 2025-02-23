import requests
import os
from dotenv import load_dotenv

load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]
        self._token = self.get_token()
        
    def get_token(self):
        header = {
    'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(
            url=TOKEN_ENDPOINT,
            data={
                "grant_type": "client_credentials",
                "client_id": self._api_key,
                "client_secret": self._api_secret
            },
            headers=header
        )
        response.raise_for_status()
        return response.json()["access_token"]
    
    def get_destination_code(self, city_name):
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS"
        }
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"No IATA code found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"KeyError: No IATA code found for {city_name}")
            return "Not Found"
        
        return code
        
 

