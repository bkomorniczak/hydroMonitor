import json
from datetime import datetime

import psycopg2
import requests

base_url_hydro = "http://danepubliczne.imgw.pl/api/data/hydro/id/"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
}

con = psycopg2.connect(
database="postgres",
user="postgres",
password="postgres",
host="localhost",
port="5432"
)


def fetch_current_station_reading(station_id):
    station_url = base_url_hydro + station_id
    response = requests.request("GET", station_url)
    return response.json()


def fetch_current_water_level(station_id):
    station_data = fetch_current_station_reading(station_id)
    current_water_level = station_data["stan_wody"]
    return current_water_level


def save_into_db_current_water_levels(station_id):
    water_level = fetch_current_water_level(station_id)
    print(water_level)
    current_time = datetime.now()
    try:
        with con.cursor() as cursor:
            sql_query = "INSERT INTO daleszyce_levels (id, czas_odczytu, stan_wody) VALUES (%s,%s,%s)"
            cursor.execute(sql_query, ('3', current_time, water_level))
        con.commit()
    finally:
        con.close()
