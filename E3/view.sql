-- 4. View
-- Create a view that summarizes the most important information regarding boat trips, combining information from different tables in the relational model. The view should have the following schema:
--  trip_info(
--     country_iso_origin, country_name_origin,
--     country_iso_dest, country_name_dest,
--     loc_name_origin,
--     loc_name_dest,
--     cni_boat,
--     country_iso_boat, country_name_boat,
--     trip_start_date)
-- Where:
-- ● country_name_origin: Foreign Key(Country)
-- ● country_name_dest: Foreign Key(Country)
-- ● country_name_boat, cni_boat: Foreign Key(Boat)

CREATE VIEW trip_info(
    country_iso_origin, country_name_origin,
    country_iso_dest, country_name_dest,
    loc_name_origin,
    loc_name_dest,
    cni_boat,
    country_iso_boat, country_name_boat,
    trip_start_date)
AS
SELECT co.iso_code AS country_iso_origin, co.name AS country_name_origin,
    cd.iso_code AS country_iso_dest, cd.name AS country_name_dest,
    lo.name AS loc_name_origin,
    ld.name AS loc_name_dest,
    cni AS cni_boat,
    cb.iso_code AS country_iso_boat, cb.name AS country_name_boat,
    t.takeoff AS trip_start_date
FROM trip t JOIN location lo
    ON (t.to_latitude, t.to_longitude) = (lo.latitude, lo.longitude)
    JOIN country co ON lo.country_name = co.name
    JOIN location ld
    ON (t.to_latitude, t.to_longitude) = (ld.latitude, ld.longitude)
    JOIN country cd ON ld.country_name = cd.name
    JOIN country cb ON t.boat_country = cb.name;

SELECT * FROM trip_info;