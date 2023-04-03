-----------------------------------------------------------------------------------------------
-- QUERY 1: Which country has more boats registered than any other?
-----------------------------------------------------------------------------------------------
SELECT country
FROM boat
GROUP by country
HAVING COUNT(*) >= ALL(
    SELECT COUNT(*)
    FROM boat
    GROUP by country
);

-----------------------------------------------------------------------------------------------
-- QUERY 2: List all the sailors that have at least two certificates
-----------------------------------------------------------------------------------------------
SELECT sailor
FROM sailing_certificate
GROUP by sailor
HAVING COUNT(*) >= 2;

-----------------------------------------------------------------------------------------------
-- QUERY 3: Who are the sailors that have sailed to every location in 'Portugal'?
-----------------------------------------------------------------------------------------------
SELECT DISTINCT skipper
FROM trip t1
WHERE NOT EXISTS(
    SELECT (latitude, longitude)
    FROM location
    WHERE country_name = 'Portugal'
    EXCEPT(
        SELECT (to_latitude, to_longitude)
        FROM trip t2
        WHERE t2.skipper = t1.skipper
    )
);

-----------------------------------------------------------------------------------------------
-- QUERY 4: List the sailors with the most skipped trips
-----------------------------------------------------------------------------------------------
SELECT skipper
FROM trip
GROUP by skipper
HAVING COUNT(*) >= ALL(
    SELECT COUNT(*)
    FROM trip
    GROUP by skipper
);

-----------------------------------------------------------------------------------------------
-- QUERY 5: List the sailors with the longest duration of trips for the same single reservation
-----------------------------------------------------------------------------------------------
SELECT reservation_start_date, reservation_end_date, boat_country, cni, skipper, sum(arrival-takeoff) AS duration
FROM trip t1
GROUP BY (reservation_start_date, reservation_end_date, boat_country, skipper, cni)
HAVING SUM(t1.arrival - t1.takeoff) >= ALL(
    SELECT SUM(t2.arrival-t2.takeoff)
    FROM trip t2
    WHERE t2.reservation_start_date = t1.reservation_start_date AND t2.reservation_end_date = t1.reservation_end_date AND t2.boat_country = t1.boat_country AND t2.cni = t1.cni
    GROUP BY (reservation_start_date, reservation_end_date, boat_country, skipper, cni)
)
ORDER BY reservation_start_date;
