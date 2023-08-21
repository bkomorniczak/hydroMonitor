import json
from datetime import datetime
import os
import psycopg2
import requests
from dotenv import load_dotenv

load_dotenv()

con = psycopg2.connect(
    database=os.getenv('POSTGRES_DATABASE'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host="localhost",
    port=os.getenv('POSTGRES_PORT')
)

base_url_hydro = "http://danepubliczne.imgw.pl/api/data/hydro/id/"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
}


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
            sql_query = "INSERT INTO daleszyce_levels (czas_odczytu, stan_wody) VALUES (%s,%s)"
            cursor.execute(sql_query, (current_time, water_level))
        con.commit()
    finally:
        con.close()
