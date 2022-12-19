-- 6. Data Analytics Queries
-- Using the view from Question 4, write two SQL queries that allow you to analyze the total number of trips according to different groups depending on:
-- 1. The start date (i.e., per year, per month independently of year, and per exact date);
-- 2. The location of origin (i.e., per location within countries, per country, and in total).
-- The submitted solution must use ROLLUP/CUBE/GROUPING SETS instructions, or the UNION of GROUP BY clauses.

-- 1. The start date (i.e., per year, per month independently of year, and per exact date);
SELECT
    EXTRACT (YEAR FROM trip_start_date) AS year,
    COUNT (*)
FROM
    trip_info
GROUP BY
        EXTRACT (YEAR FROM trip_start_date);

SELECT
    EXTRACT (MONTH FROM trip_start_date) AS month,
    COUNT (*)
FROM
    trip_info
GROUP BY
    EXTRACT (MONTH FROM trip_start_date);

SELECT
    EXTRACT (YEAR FROM trip_start_date) AS year,
    EXTRACT (MONTH FROM trip_start_date) AS month,
    EXTRACT (DAY FROM trip_start_date) AS day,
    COUNT (*)
FROM
    trip_info
GROUP BY
    EXTRACT (YEAR FROM trip_start_date),
    EXTRACT (MONTH FROM trip_start_date),
    EXTRACT (DAY FROM trip_start_date);


-- 2. The location of origin (i.e., per location within countries, per country, and in total).
SELECT
    loc_name_origin,
    COUNT (*)
FROM
    trip_info
GROUP BY loc_name_origin;

SELECT
    COALESCE(country_name_origin, 'Total'),
    COUNT (*)
FROM
    trip_info
GROUP BY ROLLUP(country_name_origin);