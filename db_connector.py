import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()
con = psycopg2.connect(
database=os.getenv('POSTGRES_DATABASE'),
user=os.getenv('POSTGRES_USER'),
password=os.getenv('POSTGRES_PASSWORD'),
host="localhost",
port=os.getenv('POSTGRES_PORT')
)

cursor_obj = con.cursor()

cursor_obj.execute("SELECT * FROM daleszyce_levels")

res = [dict(id=row[0], czas_odczytu=row[1], water_level=row[2]) for row in cursor_obj.fetchall()]


print(res)
con.close()