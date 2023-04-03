----------------------------------------------------------------------------------------------------
-- QUERY 1: The start date (i.e., per year, per month independently of year, and per exact date)
----------------------------------------------------------------------------------------------------
SELECT
    EXTRACT (YEAR FROM trip_start_date) AS year,
    EXTRACT (MONTH FROM trip_start_date) AS month,
    EXTRACT (DAY FROM trip_start_date) AS day,
    COUNT (*)
FROM trip_info
GROUP BY GROUPING SETS((year), (month), (year, month, day))
ORDER BY year, month, day;

----------------------------------------------------------------------------------------------------
-- QUERY 2: The location of origin (i.e., per location within countries, per country, and in total)
----------------------------------------------------------------------------------------------------
SELECT
    country_name_origin,
    loc_name_origin,
    COUNT (*)
FROM trip_info
GROUP BY ROLLUP(country_name_origin, loc_name_origin)
ORDER BY country_name_origin, loc_name_origin;
