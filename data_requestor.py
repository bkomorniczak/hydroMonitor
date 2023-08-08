import requests

base_url_hydro = "http://danepubliczne.imgw.pl/api/data/hydro/"
id_hydro_daleszyce = "150200160"
id_hydro_morawica = "150200120"
daleszyce_url_hydro = base_url_hydro + "/id/" + id_hydro_daleszyce
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("GET", daleszyce_url_hydro)

print(response.text)