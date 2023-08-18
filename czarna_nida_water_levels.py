import requests


station_id = ''
base_url_hydro = "http://danepubliczne.imgw.pl/api/data/hydro/id/"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }


def fetch_current_levels(station_id):
    station_url = base_url_hydro + station_id
    response = requests.request("GET", station_url)
    print(response.text)
