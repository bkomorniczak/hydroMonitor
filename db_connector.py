import psycopg2

con = psycopg2.connect(
database="postgres",
user="postgres",
password="postgres",
host="localhost",
port="5432"
)

cursor_obj = con.cursor()

cursor_obj.execute("SELECT * FROM daleszyce_levels")

res = [dict(search_word=row[0], water_level=row[2]) for row in cursor_obj.fetchall()]


print(res)
con.close()