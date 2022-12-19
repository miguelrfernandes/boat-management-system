-- Populate the database
-- country

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

-- location
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


-- boat_class
INSERT INTO boat_class(name, max_length)
VALUES ('Class A', 4.87),
    ('Class 1', 7.92),
    ('Class 2', 15.24),
    ('Class 3', 20.12),
    ('Class 4', 25.0);

-- boat
INSERT INTO boat(country, cni, name, length, boat_class, year)
VALUES ('Spain', 'ES-CNBZA653A212', 'Santa Maria', 19.0, 'Class 3', 1492),
    ('England', 'EN-CNBZA653B168', 'HMS Endeavour', 19.0, 'Class 3', 1768),
    ('France', 'FR-CNBZA653A191', 'La Recouvrance', 25.0, 'Class 4', 1991),
    ('The Netherlands', 'NL-CNBZA653A171', 'Livingstone 24', 23.99, 'Class 4', 1971),
    ('Portugal', 'PT-CNBZA653A219', 'Sessa Marine KL34 FB', 10.06, 'Class 2', 2019),
    ('Portugal', 'PT-CNBZA653A218', 'Fairline Squadron 65', 20.11, 'Class 3', 2018);


-- date_interval
INSERT INTO date_interval(start_date, end_date)
VALUES (TO_DATE('2001-03-24', 'YYYY-MM-DD'), TO_DATE('2001-07-26', 'YYYY-MM-DD')),
    (TO_DATE('2001-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD')),
    (TO_DATE('2002-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD')),
    (TO_DATE('2003-03-24', 'YYYY-MM-DD'), TO_DATE('2003-07-26', 'YYYY-MM-DD')),
    (TO_DATE('2004-03-24', 'YYYY-MM-DD'), TO_DATE('2004-07-26', 'YYYY-MM-DD')),
    (TO_DATE('2004-03-24', 'YYYY-MM-DD'), TO_DATE('2005-07-26', 'YYYY-MM-DD')),
    (TO_DATE('2005-03-24', 'YYYY-MM-DD'), TO_DATE('2005-07-26', 'YYYY-MM-DD')),
    (TO_DATE('2006-03-24', 'YYYY-MM-DD'), TO_DATE('2006-07-26', 'YYYY-MM-DD')),
    (TO_DATE('2007-03-24', 'YYYY-MM-DD'), TO_DATE('2007-07-26', 'YYYY-MM-DD')),
    (TO_DATE('2008-03-24', 'YYYY-MM-DD'), TO_DATE('2008-07-26', 'YYYY-MM-DD')),
    (TO_DATE('2009-03-24', 'YYYY-MM-DD'), TO_DATE('2009-07-26', 'YYYY-MM-DD'));

-- sailor
INSERT INTO sailor(email, firstname, surname)
VALUES ('columbus@email.com', 'Christopher', 'Columbus'),
    ('popeye@email.com', 'Popeye', 'Sailor Man'),
    ('jacksparrow@email.com', 'Jack', 'Sparrow'),
    ('john@email.com', 'John', 'Smith'),
    ('bob@email.com', 'Bob', 'Ross'),
    ('harry@hogwarts.com', 'Harry', 'Potter'),
    ('hermione@hogwarts.com', 'Hermione', 'Granger'),
    ('ron@hogwarts.com', 'Ron', 'Weasley'),
    ('dumbledore@hogwarts.com', 'Albus', 'Dumbledore'),
    ('joaosantos@email.com', 'Joao', 'Santos'),
    ('joaomanuel@email.com', 'Joao', 'Santos');

-- senior
INSERT INTO senior(email)
VALUES ('columbus@email.com'),
    ('dumbledore@hogwarts.com'),
    ('harry@hogwarts.com'),
    ('popeye@email.com'),
    ('joaosantos@email.com');

-- junior
INSERT INTO junior(email)
VALUES ('jacksparrow@email.com'),
    ('ron@hogwarts.com'),
    ('hermione@hogwarts.com'),
    ('bob@email.com'),
    ('john@email.com');

-- sailing_certificate
INSERT INTO sailing_certificate(sailor, issue_date, expiry_date, boat_class)
VALUES ('columbus@email.com', TO_TIMESTAMP('1999-03-24 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2009-03-25', 'YYYY-MM-DD'), 'Class 3'),
    ('jacksparrow@email.com', TO_TIMESTAMP('1998-06-21 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2008-06-22', 'YYYY-MM-DD'), 'Class 4'),
    ('popeye@email.com', TO_TIMESTAMP('2000-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2010-03-25', 'YYYY-MM-DD'), 'Class 3'),
    ('dumbledore@hogwarts.com', TO_TIMESTAMP('2001-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2011-03-25', 'YYYY-MM-DD'), 'Class 3'),
    ('dumbledore@hogwarts.com', TO_TIMESTAMP('2002-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2012-03-25', 'YYYY-MM-DD'), 'Class 4'),
    ('hermione@hogwarts.com', TO_TIMESTAMP('2003-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2013-03-25', 'YYYY-MM-DD'), 'Class 2');

-- valid_for
INSERT INTO valid_for(sailor, issue_date, country_name)
VALUES ('columbus@email.com', TO_TIMESTAMP('1999-03-24 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'England'),
    ('columbus@email.com', TO_TIMESTAMP('1999-03-24 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Portugal'),
    ('popeye@email.com', TO_TIMESTAMP('2000-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Spain'),
    ('dumbledore@hogwarts.com', TO_TIMESTAMP('2001-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'England'),
    ('dumbledore@hogwarts.com', TO_TIMESTAMP('2002-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Portugal'),
    ('jacksparrow@email.com', TO_TIMESTAMP('1998-06-21 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'France'),
    ('hermione@hogwarts.com', TO_TIMESTAMP('2003-03-24 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'The Netherlands');

-- reservation
INSERT INTO reservation(country, cni, start_date, end_date, responsible)
VALUES ('Spain', 'ES-CNBZA653A212', TO_DATE('2001-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD'), 'columbus@email.com'),
    ('England', 'EN-CNBZA653B168', TO_DATE('2002-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD'), 'popeye@email.com'),
    ('France', 'FR-CNBZA653A191', TO_DATE('2004-03-24', 'YYYY-MM-DD'), TO_DATE('2005-07-26', 'YYYY-MM-DD'), 'harry@hogwarts.com'),
    ('Portugal', 'PT-CNBZA653A219', TO_DATE('2006-03-24', 'YYYY-MM-DD'), TO_DATE('2006-07-26', 'YYYY-MM-DD'), 'joaosantos@email.com'),
    ('Portugal', 'PT-CNBZA653A219', TO_DATE('2007-03-24', 'YYYY-MM-DD'), TO_DATE('2007-07-26', 'YYYY-MM-DD'), 'popeye@email.com'),
    ('Portugal', 'PT-CNBZA653A218', TO_DATE('2008-03-24', 'YYYY-MM-DD'), TO_DATE('2008-07-26', 'YYYY-MM-DD'), 'popeye@email.com');

-- trip
INSERT INTO trip(boat_country, cni, reservation_start_date, reservation_end_date, takeoff, arrival, insurance, from_latitude, from_longitude, to_latitude, to_longitude, skipper)
VALUES ('Spain', 'ES-CNBZA653A212', TO_DATE('2001-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD'), TO_DATE('2001-03-27', 'YYYY-MM-DD'), TO_DATE('2001-07-23', 'YYYY-MM-DD'), 'IN-123456789', 38.736946, -9.142685, 37.019356, -7.930440, 'columbus@email.com'),
    ('Spain', 'ES-CNBZA653A212', TO_DATE('2001-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD'), TO_DATE('2002-03-27', 'YYYY-MM-DD'), TO_DATE('2002-07-23', 'YYYY-MM-DD'), 'IN-123456789', 41.385064, 2.173403, 39.469907, -0.377398, 'popeye@email.com'),
    ('England', 'EN-CNBZA653B168', TO_DATE('2002-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD'), TO_DATE('2002-03-27', 'YYYY-MM-DD'), TO_DATE('2002-07-23', 'YYYY-MM-DD'), 'IN-123456789', 51.507351, -0.127758, 53.480759, -2.242631, 'dumbledore@hogwarts.com'),
    ('France', 'FR-CNBZA653A191', TO_DATE('2004-03-24', 'YYYY-MM-DD'), TO_DATE('2005-07-26', 'YYYY-MM-DD'), TO_DATE('2004-03-27', 'YYYY-MM-DD'), TO_DATE('2004-07-23', 'YYYY-MM-DD'), 'IN-123456789', 51.926517, 4.462456, 52.377956, 4.897070, 'ron@hogwarts.com'),
    ('France', 'FR-CNBZA653A191', TO_DATE('2004-03-24', 'YYYY-MM-DD'), TO_DATE('2005-07-26', 'YYYY-MM-DD'), TO_DATE('2005-03-27', 'YYYY-MM-DD'), TO_DATE('2005-07-23', 'YYYY-MM-DD'), 'IN-123456789', 38.736946, -9.142685, 41.385064, 2.173403, 'hermione@hogwarts.com'),
    ('Spain', 'ES-CNBZA653A212', TO_DATE('2001-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD'), TO_DATE('2001-03-28', 'YYYY-MM-DD'), TO_DATE('2001-07-23', 'YYYY-MM-DD'), 'IN-123456789', 38.736946, -9.142685, 40.416775, -3.703790, 'columbus@email.com'),
    ('Spain', 'ES-CNBZA653A212', TO_DATE('2001-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD'), TO_DATE('2001-03-29', 'YYYY-MM-DD'), TO_DATE('2001-07-23', 'YYYY-MM-DD'), 'IN-123456789', 38.736946, -9.142685, 41.385064, 2.173403, 'columbus@email.com'),
    ('Spain', 'ES-CNBZA653A212', TO_DATE('2001-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD'), TO_DATE('2001-03-30', 'YYYY-MM-DD'), TO_DATE('2001-07-23', 'YYYY-MM-DD'), 'IN-123456789', 38.736946, -9.142685, 39.469907, -0.377398, 'columbus@email.com');

-- authorised
INSERT INTO authorised(sailor, boat_country, cni, start_date, end_date)
VALUES ('columbus@email.com', 'Spain', 'ES-CNBZA653A212', TO_DATE('2001-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD')),
    ('jacksparrow@email.com', 'Spain', 'ES-CNBZA653A212', TO_DATE('2001-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD')),
    ('popeye@email.com', 'Spain', 'ES-CNBZA653A212', TO_DATE('2001-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD')),
    ('popeye@email.com','England', 'EN-CNBZA653B168', TO_DATE('2002-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD')),
    ('dumbledore@hogwarts.com','England', 'EN-CNBZA653B168', TO_DATE('2002-03-24', 'YYYY-MM-DD'), TO_DATE('2002-07-26', 'YYYY-MM-DD')),
    ('hermione@hogwarts.com','France', 'FR-CNBZA653A191', TO_DATE('2004-03-24', 'YYYY-MM-DD'), TO_DATE('2005-07-26', 'YYYY-MM-DD')),
    ('harry@hogwarts.com','France', 'FR-CNBZA653A191', TO_DATE('2004-03-24', 'YYYY-MM-DD'), TO_DATE('2005-07-26', 'YYYY-MM-DD')),
    ('ron@hogwarts.com','France', 'FR-CNBZA653A191', TO_DATE('2004-03-24', 'YYYY-MM-DD'), TO_DATE('2005-07-26', 'YYYY-MM-DD')),
    ('joaosantos@email.com','Portugal', 'PT-CNBZA653A219', TO_DATE('2006-03-24', 'YYYY-MM-DD'), TO_DATE('2006-07-26', 'YYYY-MM-DD')),
    ('harry@hogwarts.com','Portugal', 'PT-CNBZA653A219', TO_DATE('2006-03-24', 'YYYY-MM-DD'), TO_DATE('2006-07-26', 'YYYY-MM-DD')),
    ('popeye@email.com', 'Portugal', 'PT-CNBZA653A219', TO_DATE('2007-03-24', 'YYYY-MM-DD'), TO_DATE('2007-07-26', 'YYYY-MM-DD'));