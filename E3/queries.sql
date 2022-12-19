-- SQL 1
-- Which country has more boats registered than any other?
SELECT country
FROM boat
GROUP BY country
HAVING COUNT(cni) >= ALL(
    SELECT COUNT(cni)
    FROM boat
    GROUP BY country
);

-- SQL 2
-- 2. List all the sailors that have at least two certificates.
SELECT sailor
FROM sailing_certificate
GROUP BY sailor
HAVING COUNT(issue_date) >= 2;

-- SQL 3
-- 3. Who are the sailors that have sailed to every location in 'Portugal'?
SELECT skipper
FROM trip
EXCEPT ALL
SELECT skipper
FROM (SELECT skipper, to_latitude, to_longitude
        FROM trip, location
        EXCEPT ALL
        SELECT skipper, latitude,longitude FROM trip NATURAL JOIN location
        WHERE country_name = 'Portugal'
) AS not_having_sailed_every_location_in_Portugal;

-- SQL 4
-- 4. List the sailors with the most skipped trips.
SELECT skipper
FROM trip
GROUP BY skipper
HAVING COUNT(reservation_start_date) >= ALL(
    SELECT COUNT(reservation_start_date)
    FROM trip
    GROUP BY skipper
);

-- SQL 5
-- 5. List the sailors with the longest duration of trips (sum of trip durations) for the same single reservation; display also the sum of the trips duration.
SELECT skipper, SUM(t.arrival - t.takeoff)
    FROM trip t JOIN reservation r
    ON (t.reservation_start_date, t.reservation_end_date) = (r.start_date, r.end_date)
    WHERE t.skipper = r.responsible
    GROUP BY skipper
HAVING SUM(t.arrival - t.takeoff) >= ALL(
    SELECT SUM(t.arrival - t.takeoff)
    FROM trip t JOIN reservation r
    ON (t.reservation_start_date, t.reservation_end_date) = (r.start_date, r.end_date)
    WHERE t.skipper = r.responsible
    GROUP BY skipper
);
