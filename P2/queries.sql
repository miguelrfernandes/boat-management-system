-------------------------QUERY A)-------------------------------
SELECT boat_name
FROM boat
WHERE (country_name, cin) IN (
    SELECT DISTINCT boat_country_name, boat_cin
    FROM trip);

-------------------------QUERY B)-------------------------------
SELECT boat_name
FROM boat
WHERE (country_name, cin) NOT IN (
    SELECT DISTINCT boat_country_name, boat_cin
    FROM trip);

-------------------------QUERY C)-------------------------------
SELECT boat_name
FROM boat b
JOIN country c
    ON c.name= b.country_name
WHERE (iso_code ='PRT') AND ((country_name, cin) IN (
    SELECT DISTINCT boat_country_name, boat_cin
    FROM reservation r
    JOIN sailor s
        ON s.email = r.responsible_sailor_email
    WHERE surname LIKE '%Santos'));

-------------------------QUERY D)-------------------------------
SELECT DISTINCT first_name, surname, email
FROM sailor s
JOIN trip t
    ON s.email = t.skipper_email
JOIN boat b
    ON b.country_name = t.boat_country_name AND b.cin = t.boat_cin
WHERE (skipper_email, class_name) NOT IN (
    SELECT sailor_email, for_class_name
    FROM sailing_certificate);
