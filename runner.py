import czarna_nida_water_levels

id_hydro_daleszyce = "150200160"

# print(czarna_nida_water_levels.fetch_current_water_level(id_hydro_daleszyce))
czarna_nida_water_levels.save_into_db_current_water_levels(id_hydro_daleszyce)