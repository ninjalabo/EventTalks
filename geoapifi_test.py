import requests
from requests.structures import CaseInsensitiveDict

#url = "https://api.geoapify.com/v1/routing?waypoints=50.96209827745463%2C4.414458883409225%7C50.429137079078345%2C5.00088081232559&mode=drive&apiKey=db60adfdd3ba4fdcad1e9e5951276ca8"
#url= "https://api.geoapify.com/v1/routing?apiKey=db60adfdd3ba4fdcad1e9e5951276ca8&waypoints=60.21169%2C25.14557%7C60.158683%2C24.733938&mode=bicycle&details=route_details"
url= "https://api.geoapify.com/v1/routing?apiKey=db60adfdd3ba4fdcad1e9e5951276ca8&waypoints=60.2056%2C25.1450%7C60.1822%2C24.8040&mode=bicycle&details=route_details"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(url, headers=headers)

print(resp.status_code)
print(resp)