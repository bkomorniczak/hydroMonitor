CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


CREATE TABLE daleszyce_levels (
    daleszyce_station_id uuid DEFAULT uuid_generate_v4 (),
    czas_odczytu timestamp,
    stan_wody int,
    PRIMARY KEY(daleszyce_station_id)
);

CREATE TABLE morawica_levels (
    morawica_station_id uuid DEFAULT uuid_generate_v4 (),
    czas_odczytu timestamp,
    stan_wody int,
    PRIMARY KEY(morawica_station_id)
);




