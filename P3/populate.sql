----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table country
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO country(name, flag, ISO_code)
VALUES ('Portugal', 'https://laendercode.net/img/flag-icon-css/flags/4x3/pt.svg', 'PRT'),
    ('Spain', 'https://laendercode.net/img/flag-icon-css/flags/4x3/es.svg', 'ESP'),
    ('England', 'https://laendercode.net/img/flag-icon-css/flags/4x3/en.svg', 'ENG'),
    ('France', 'https://laendercode.net/img/flag-icon-css/flags/4x3/fr.svg', 'FRA'),
    ('Italy', 'https://laendercode.net/img/flag-icon-css/flags/4x3/it.svg', 'ITA'),
    ('Russia', 'https://laendercode.net/img/flag-icon-css/flags/4x3/ru.svg', 'RUS'),
    ('Brazil', 'https://laendercode.net/img/flag-icon-css/flags/4x3/br.svg', 'BRA'),
    ('China', 'https://laendercode.net/img/flag-icon-css/flags/4x3/cn.svg', 'CHN'),
    ('India', 'https://laendercode.net/img/flag-icon-css/flags/4x3/in.svg', 'IND'),
    ('United States', 'https://laendercode.net/img/flag-icon-css/flags/4x3/us.svg', 'USA'),
    ('Canada', 'https://laendercode.net/img/flag-icon-css/flags/4x3/ca.svg', 'CAN'),
    ('Germany', 'https://laendercode.net/img/flag-icon-css/flags/4x3/de.svg', 'DEU'),
    ('Japan', 'https://laendercode.net/img/flag-icon-css/flags/4x3/jp.svg', 'JPN'),
    ('South Korea', 'https://laendercode.net/img/flag-icon-css/flags/4x3/kr.svg', 'KOR'),
    ('Mexico', 'https://laendercode.net/img/flag-icon-css/flags/4x3/mx.svg', 'MEX'),
    ('South Africa', 'https://laendercode.net/img/flag-icon-css/flags/4x3/za.svg', 'ZAF'),
    ('Egypt', 'https://laendercode.net/img/flag-icon-css/flags/4x3/eg.svg', 'EGY'),
    ('Iran', 'https://laendercode.net/img/flag-icon-css/flags/4x3/ir.svg', 'IRN'),
    ('Afghanistan', 'https://laendercode.net/img/flag-icon-css/flags/4x3/af.svg', 'AFG'),
    ('Albania', 'https://laendercode.net/img/flag-icon-css/flags/4x3/al.svg', 'ALB'),
    ('Algeria', 'https://laendercode.net/img/flag-icon-css/flags/4x3/dz.svg', 'DZA'),
    ('American Samoa', 'https://laendercode.net/img/flag-icon-css/flags/4x3/as.svg', 'ASM'),
    ('Andorra', 'https://laendercode.net/img/flag-icon-css/flags/4x3/ad.svg', 'AND'),
    ('Angola', 'https://laendercode.net/img/flag-icon-css/flags/4x3/ao.svg', 'AGO'),
    ('Anguilla', 'https://laendercode.net/img/flag-icon-css/flags/4x3/ai.svg', 'AIA'),
    ('Antarctica', 'https://laendercode.net/img/flag-icon-css/flags/4x3/aq.svg', 'ATA'),
    ('Antigua and Barbuda', 'https://laendercode.net/img/flag-icon-css/flags/4x3/ag.svg', 'ATG'),
    ('Argentina', 'https://laendercode.net/img/flag-icon-css/flags/4x3/ar.svg', 'ARG'),
    ('Armenia', 'https://laendercode.net/img/flag-icon-css/flags/4x3/am.svg', 'ARM'),
    ('Aruba', 'https://laendercode.net/img/flag-icon-css/flags/4x3/aw.svg', 'ABW'),
    ('Australia', 'https://laendercode.net/img/flag-icon-css/flags/4x3/au.svg', 'AUS'),
    ('Austria', 'https://laendercode.net/img/flag-icon-css/flags/4x3/at.svg', 'AUT'),
    ('Azerbaijan', 'https://laendercode.net/img/flag-icon-css/flags/4x3/az.svg', 'AZE'),
    ('Bahamas', 'https://laendercode.net/img/flag-icon-css/flags/4x3/bs.svg', 'BHS'),
    ('Bahrain', 'https://laendercode.net/img/flag-icon-css/flags/4x3/bh.svg', 'BHR'),
    ('The Netherlands', 'https://laendercode.net/img/flag-icon-css/flags/4x3/nl.svg', 'NLD');


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table location
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO location(latitude, longitude, name, country_name)
VALUES (38.736946, -9.142685, 'Lisboa', 'Portugal'),
    (37.019356, -7.930440, 'Faro', 'Portugal'),
    (40.416775, -3.703790, 'Madrid', 'Spain'),
    (41.385064, 2.173403, 'Barcelona', 'Spain'),
    (39.469907, -0.377398, 'Valencia', 'Spain'),
    (48.856614, 2.352222, 'Paris', 'France'),
    (45.764043, 4.835659, 'Lyon', 'France'),
    (43.296482, 5.369780, 'Marseille', 'France'),
    (51.507351, -0.127758, 'London', 'England'),
    (53.480759, -2.242631, 'Manchester', 'England'),
    (41.902782, 12.496366, 'Rome', 'Italy'),
    (45.464211, 9.189982, 'Milan', 'Italy'),
    (45.440847, 12.315515, 'Venice', 'Italy'),
    (52.520008, 13.404954, 'Berlin', 'Germany'),
    (53.551086, 9.993682, 'Hamburg', 'Germany'),
    (53.079296, 8.801694, 'Bremen', 'Germany'),
    (55.755826, 37.617300, 'Moscow', 'Russia'),
    (59.934280, 30.335099, 'Saint Petersburg', 'Russia'),
    (55.041500, 82.934600, 'Novosibirsk', 'Russia'),
    (-15.794228, -47.882166, 'Brasilia', 'Brazil'),
    (-22.906847, -43.172896, 'Rio de Janeiro', 'Brazil'),
    (-23.550651, -46.633382, 'São Paulo', 'Brazil'),
    (-33.868820, 151.209290, 'Sydney', 'Australia'),
    (-37.813628, 144.963058, 'Melbourne', 'Australia'),
    (-31.950527, 115.860458, 'Perth', 'Australia'),
    (31.224361, 121.469170, 'Shanghai', 'China'),
    (39.133331, 117.183334, 'Tianjin', 'China'),
    (51.926517, 4.462456, 'Rotterdam', 'The Netherlands'),
    (52.377956, 4.897070, 'Amsterdam', 'The Netherlands');


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table boat_class
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO boat_class(name, max_length)
VALUES ('Class A', 4.87),
    ('Class 1', 7.92),
    ('Class 2', 15.24),
    ('Class 3', 20.12),
    ('Class 4', 25.0);


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table boat
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO boat(country, cni, name, length, boat_class, year)
VALUES ('Spain', 'CNBZA653A212', 'Santa Maria', 19.0, 'Class 3', 1492),
    ('England', 'CNBZA653B168', 'HMS Endeavour', 19.0, 'Class 3', 1768),
    ('France', 'CNBZA653A191', 'La Recouvrance', 25.0, 'Class 4', 1991),
    ('The Netherlands', 'CNBZA653A171', 'Livingstone 24', 23.99, 'Class 4', 1971),
    ('Portugal', 'CNBZA653A219', 'Sessa Marine KL34 FB', 10.06, 'Class 2', 2019),
    ('Portugal', 'CNBZA653A218', 'Fairline Squadron 65', 20.11, 'Class 3', 2018),
    ('Portugal', 'CNBZA653A217', 'Vasco da Gama 45', 11.33, 'Class 2', 2015);


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table date_interval
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO date_interval(start_date, end_date)
VALUES(TO_DATE('2016-04-10', 'YYYY-MM-DD'), TO_DATE('2017-02-01', 'YYYY-MM-DD')),
    (TO_DATE('2017-03-24', 'YYYY-MM-DD'), TO_DATE('2017-05-15', 'YYYY-MM-DD')),
    (TO_DATE('2019-11-08', 'YYYY-MM-DD'), TO_DATE('2020-07-26', 'YYYY-MM-DD')),
    (TO_DATE('2020-01-01', 'YYYY-MM-DD'), TO_DATE('2020-03-31', 'YYYY-MM-DD')),
    (TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-01-05', 'YYYY-MM-DD'));


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table sailor
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO sailor(email, firstname, surname)
VALUES ('columbus@email.com', 'Christopher', 'Columbus'),
    ('popeye@email.com', 'Popeye', 'Sailor Man'),
    ('jacksparrow@email.com', 'Jack', 'Sparrow'),
    ('john@email.com', 'John', 'Smith'),
    ('bob@email.com', 'Bob', 'Ross'),
    ('harry@hogwarts.com', 'Harry', 'Potter'),
    ('hermione@hogwarts.com', 'Hermione', 'Granger'),
    ('ron@hogwarts.com', 'Ron', 'Weasley'),
    ('dumbledore@hogwarts.com', 'Albus', 'Dumbledore');

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table senior
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO senior(email)
VALUES ('columbus@email.com'),
    ('dumbledore@hogwarts.com'),
    ('harry@hogwarts.com'),
    ('popeye@email.com');


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table junior
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO junior(email)
VALUES ('jacksparrow@email.com'),
    ('ron@hogwarts.com'),
    ('hermione@hogwarts.com'),
    ('bob@email.com'),
    ('john@email.com');


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table sailing_certificate
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO sailing_certificate(sailor, issue_date, expiry_date, boat_class)
VALUES ('columbus@email.com', TO_TIMESTAMP('1999-03-24 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2025-03-25', 'YYYY-MM-DD'), 'Class 3'),
    ('jacksparrow@email.com', TO_TIMESTAMP('1998-06-21 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2023-06-22', 'YYYY-MM-DD'), 'Class 4'),
    ('popeye@email.com', TO_TIMESTAMP('2011-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2024-03-25', 'YYYY-MM-DD'), 'Class 3'),
    ('dumbledore@hogwarts.com', TO_TIMESTAMP('2016-01-10 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2026-06-07', 'YYYY-MM-DD'), 'Class 3'),
    ('dumbledore@hogwarts.com', TO_TIMESTAMP('2014-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2025-04-01', 'YYYY-MM-DD'), 'Class 4'),
    ('hermione@hogwarts.com', TO_TIMESTAMP('2015-09-10 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2024-07-15', 'YYYY-MM-DD'), 'Class 2'),
    ('hermione@hogwarts.com', TO_TIMESTAMP('2015-05-07 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2025-12-31', 'YYYY-MM-DD'), 'Class 1'),
    ('hermione@hogwarts.com', TO_TIMESTAMP('2015-10-01 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2024-07-04', 'YYYY-MM-DD'), 'Class 3'),
    ('john@email.com', TO_TIMESTAMP('2013-05-01 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2027-02-28', 'YYYY-MM-DD'), 'Class 2'),
    ('bob@email.com', TO_TIMESTAMP('2018-01-01 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2030-02-28', 'YYYY-MM-DD'), 'Class A'),
    ('bob@email.com', TO_TIMESTAMP('2016-01-01 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2028-02-28', 'YYYY-MM-DD'), 'Class 2');



----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table valid_for
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO valid_for(sailor, issue_date, country_name)
VALUES ('columbus@email.com', TO_TIMESTAMP('1999-03-24 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'England'),
    ('columbus@email.com', TO_TIMESTAMP('1999-03-24 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Portugal'),
    ('jacksparrow@email.com', TO_TIMESTAMP('1998-06-21 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'France'),
    ('popeye@email.com', TO_TIMESTAMP('2011-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Spain'),
    ('dumbledore@hogwarts.com', TO_TIMESTAMP('2014-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Portugal'),
    ('dumbledore@hogwarts.com', TO_TIMESTAMP('2016-01-10 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'England'),
    ('hermione@hogwarts.com', TO_TIMESTAMP('2015-09-10 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'The Netherlands'),
    ('hermione@hogwarts.com', TO_TIMESTAMP('2015-09-10 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'China'),
    ('hermione@hogwarts.com', TO_TIMESTAMP('2015-05-07 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Australia'),
    ('hermione@hogwarts.com', TO_TIMESTAMP('2015-10-01 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Brazil'),
    ('john@email.com', TO_TIMESTAMP('2013-05-01 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Russia'),
    ('bob@email.com', TO_TIMESTAMP('2018-01-01 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Italy'),
    ('bob@email.com', TO_TIMESTAMP('2016-01-01 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Portugal');


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table reservation
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO reservation(country, cni, start_date, end_date, responsible)
VALUES ('Spain', 'CNBZA653A212', TO_DATE('2016-04-10', 'YYYY-MM-DD'), TO_DATE('2017-02-01', 'YYYY-MM-DD'), 'columbus@email.com'),
    ('England', 'CNBZA653B168', TO_DATE('2017-03-24', 'YYYY-MM-DD'), TO_DATE('2017-05-15', 'YYYY-MM-DD'), 'popeye@email.com'),
    ('France', 'CNBZA653A191', TO_DATE('2019-11-08', 'YYYY-MM-DD'), TO_DATE('2020-07-26', 'YYYY-MM-DD'), 'harry@hogwarts.com'),
    ('The Netherlands', 'CNBZA653A171', TO_DATE('2020-01-01', 'YYYY-MM-DD'), TO_DATE('2020-03-31', 'YYYY-MM-DD'), 'dumbledore@hogwarts.com'),
    ('Portugal', 'CNBZA653A217', TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-01-05', 'YYYY-MM-DD'), 'columbus@email.com');


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table trip
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO trip(boat_country, cni, reservation_start_date, reservation_end_date, takeoff, arrival, insurance, from_latitude, from_longitude, to_latitude, to_longitude, skipper)
VALUES ('Spain', 'CNBZA653A212', TO_DATE('2016-04-10', 'YYYY-MM-DD'), TO_DATE('2017-02-01', 'YYYY-MM-DD'), TO_DATE('2016-04-12', 'YYYY-MM-DD'), TO_DATE('2016-06-01', 'YYYY-MM-DD'), 'IN-123456789', 38.736946, -9.142685, 37.019356, -7.930440, 'hermione@hogwarts.com'),
    ('Spain', 'CNBZA653A212', TO_DATE('2016-04-10', 'YYYY-MM-DD'), TO_DATE('2017-02-01', 'YYYY-MM-DD'), TO_DATE('2016-08-05', 'YYYY-MM-DD'), TO_DATE('2017-01-31', 'YYYY-MM-DD'), 'IN-123456789', 41.385064, 2.173403, 39.469907, -0.377398, 'popeye@email.com'),
    ('England', 'CNBZA653B168', TO_DATE('2017-03-24', 'YYYY-MM-DD'), TO_DATE('2017-05-15', 'YYYY-MM-DD'), TO_DATE('2017-03-27', 'YYYY-MM-DD'), TO_DATE('2017-04-05', 'YYYY-MM-DD'), 'IN-123456789', -15.794228, -47.882166, -22.906847, -43.172896, 'dumbledore@hogwarts.com'),
    ('England', 'CNBZA653B168', TO_DATE('2017-03-24', 'YYYY-MM-DD'), TO_DATE('2017-05-15', 'YYYY-MM-DD'), TO_DATE('2017-04-10', 'YYYY-MM-DD'), TO_DATE('2017-04-15', 'YYYY-MM-DD'), 'IN-123456789', -22.906847, -43.172896, -23.550651, -46.633382, 'columbus@email.com'),
    ('England', 'CNBZA653B168', TO_DATE('2017-03-24', 'YYYY-MM-DD'), TO_DATE('2017-05-15', 'YYYY-MM-DD'), TO_DATE('2017-04-20', 'YYYY-MM-DD'), TO_DATE('2017-05-05', 'YYYY-MM-DD'), 'IN-123456789', -23.550651, -46.633382, -15.794228, -47.882166, 'popeye@email.com'),
    ('France', 'CNBZA653A191', TO_DATE('2019-11-08', 'YYYY-MM-DD'), TO_DATE('2020-07-26', 'YYYY-MM-DD'), TO_DATE('2020-02-01', 'YYYY-MM-DD'), TO_DATE('2020-07-01', 'YYYY-MM-DD'), 'IN-123456789', 55.041500, 82.934600, 39.133331, 117.183334, 'jacksparrow@email.com'),
    ('The Netherlands', 'CNBZA653A171', TO_DATE('2020-01-01', 'YYYY-MM-DD'), TO_DATE('2020-03-31', 'YYYY-MM-DD'), TO_DATE('2020-01-01', 'YYYY-MM-DD'), TO_DATE('2020-01-25', 'YYYY-MM-DD'), 'IN-123456789', -22.906847, -43.172896, 31.224361, 121.469170, 'jacksparrow@email.com'),
    ('The Netherlands', 'CNBZA653A171', TO_DATE('2020-01-01', 'YYYY-MM-DD'), TO_DATE('2020-03-31', 'YYYY-MM-DD'), TO_DATE('2020-01-30', 'YYYY-MM-DD'), TO_DATE('2020-02-15', 'YYYY-MM-DD'), 'IN-123456789', -31.950527, 115.860458, 53.551086, 9.993682, 'jacksparrow@email.com'),
    ('The Netherlands', 'CNBZA653A171', TO_DATE('2020-01-01', 'YYYY-MM-DD'), TO_DATE('2020-03-31', 'YYYY-MM-DD'), TO_DATE('2020-02-17', 'YYYY-MM-DD'), TO_DATE('2020-03-10', 'YYYY-MM-DD'), 'IN-123456789', 59.934280, 30.335099, 55.755826, 37.617300, 'dumbledore@hogwarts.com'),
    ('Portugal', 'CNBZA653A217', TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-01-05', 'YYYY-MM-DD'), TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2022-12-15', 'YYYY-MM-DD'), 'IN-123456789', 41.385064, 2.173403, 40.416775, -3.703790, 'john@email.com'),
    ('Portugal', 'CNBZA653A217', TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-01-05', 'YYYY-MM-DD'), TO_DATE('2022-12-20', 'YYYY-MM-DD'), TO_DATE('2022-12-23', 'YYYY-MM-DD'), 'IN-123456789', 40.416775, -3.703790, 38.736946, -9.142685, 'hermione@hogwarts.com'),
    ('Portugal', 'CNBZA653A217', TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-01-05', 'YYYY-MM-DD'), TO_DATE('2022-12-27', 'YYYY-MM-DD'), TO_DATE('2022-12-31', 'YYYY-MM-DD'), 'IN-123456789', 38.736946, -9.142685, 41.902782, 12.496366, 'hermione@hogwarts.com');


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- table authorised
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO authorised(sailor, boat_country, cni, start_date, end_date)
VALUES ('columbus@email.com', 'Spain', 'CNBZA653A212', TO_DATE('2016-04-10', 'YYYY-MM-DD'), TO_DATE('2017-02-01', 'YYYY-MM-DD')),
    ('jacksparrow@email.com', 'Spain', 'CNBZA653A212', TO_DATE('2016-04-10', 'YYYY-MM-DD'), TO_DATE('2017-02-01', 'YYYY-MM-DD')),
    ('popeye@email.com', 'Spain', 'CNBZA653A212', TO_DATE('2016-04-10', 'YYYY-MM-DD'), TO_DATE('2017-02-01', 'YYYY-MM-DD')),
    ('hermione@hogwarts.com', 'Spain', 'CNBZA653A212', TO_DATE('2016-04-10', 'YYYY-MM-DD'), TO_DATE('2017-02-01', 'YYYY-MM-DD')),
    ('popeye@email.com','England', 'CNBZA653B168', TO_DATE('2017-03-24', 'YYYY-MM-DD'), TO_DATE('2017-05-15', 'YYYY-MM-DD')),
    ('dumbledore@hogwarts.com','England', 'CNBZA653B168', TO_DATE('2017-03-24', 'YYYY-MM-DD'), TO_DATE('2017-05-15', 'YYYY-MM-DD')),
    ('columbus@email.com','England', 'CNBZA653B168', TO_DATE('2017-03-24', 'YYYY-MM-DD'), TO_DATE('2017-05-15', 'YYYY-MM-DD')),
    ('bob@email.com','England', 'CNBZA653B168', TO_DATE('2017-03-24', 'YYYY-MM-DD'), TO_DATE('2017-05-15', 'YYYY-MM-DD')),
    ('hermione@hogwarts.com','France', 'CNBZA653A191', TO_DATE('2019-11-08', 'YYYY-MM-DD'), TO_DATE('2020-07-26', 'YYYY-MM-DD')),
    ('harry@hogwarts.com','France', 'CNBZA653A191', TO_DATE('2019-11-08', 'YYYY-MM-DD'), TO_DATE('2020-07-26', 'YYYY-MM-DD')),
    ('ron@hogwarts.com','France', 'CNBZA653A191', TO_DATE('2019-11-08', 'YYYY-MM-DD'), TO_DATE('2020-07-26', 'YYYY-MM-DD')),
    ('jacksparrow@email.com','France', 'CNBZA653A191', TO_DATE('2019-11-08', 'YYYY-MM-DD'), TO_DATE('2020-07-26', 'YYYY-MM-DD')),
    ('hermione@hogwarts.com', 'The Netherlands', 'CNBZA653A171', TO_DATE('2020-01-01', 'YYYY-MM-DD'), TO_DATE('2020-03-31', 'YYYY-MM-DD')),
    ('dumbledore@hogwarts.com', 'The Netherlands', 'CNBZA653A171', TO_DATE('2020-01-01', 'YYYY-MM-DD'), TO_DATE('2020-03-31', 'YYYY-MM-DD')),
    ('jacksparrow@email.com', 'The Netherlands', 'CNBZA653A171', TO_DATE('2020-01-01', 'YYYY-MM-DD'), TO_DATE('2020-03-31', 'YYYY-MM-DD')),
    ('john@email.com', 'The Netherlands', 'CNBZA653A171', TO_DATE('2020-01-01', 'YYYY-MM-DD'), TO_DATE('2020-03-31', 'YYYY-MM-DD')),
    ('columbus@email.com', 'Portugal', 'CNBZA653A217', TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-01-05', 'YYYY-MM-DD')),
    ('ron@hogwarts.com', 'Portugal', 'CNBZA653A217', TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-01-05', 'YYYY-MM-DD')),
    ('popeye@email.com', 'Portugal', 'CNBZA653A217', TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-01-05', 'YYYY-MM-DD')),
    ('jacksparrow@email.com', 'Portugal', 'CNBZA653A217', TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-01-05', 'YYYY-MM-DD')),
    ('john@email.com', 'Portugal', 'CNBZA653A217', TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-01-05', 'YYYY-MM-DD')),
    ('hermione@hogwarts.com', 'Portugal', 'CNBZA653A217', TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-01-05', 'YYYY-MM-DD'));

