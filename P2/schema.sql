DROP TABLE IF EXISTS authorised;
DROP TABLE IF EXISTS valid_for;
DROP TABLE IF EXISTS trip;
DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS boat;
DROP TABLE IF EXISTS sailing_certificate;
DROP TABLE IF EXISTS boat_class;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS junior;
DROP TABLE IF EXISTS senior;
DROP TABLE IF EXISTS sailor;
DROP TABLE IF EXISTS date_interval;

CREATE TABLE date_interval(
    start_date DATE,
    end_date DATE,
    PRIMARY KEY(start_date, end_date)
);

CREATE TABLE sailor(
    email VARCHAR(254),
    first_name VARCHAR(80) NOT NULL,
    surname VARCHAR(80) NOT NULL,
    PRIMARY KEY(email)
    -- Every Sailor must exist either in the table 'senior' or in the table 'junior'
);

CREATE TABLE senior(
    email VARCHAR(254),
    PRIMARY KEY(email),
    FOREIGN KEY(email) REFERENCES sailor(email)
    -- Every Sailor must exist either in the table 'senior' or in the table 'junior'
    -- No Senior can exist in the table 'junior'
);

CREATE TABLE junior(
    email VARCHAR(254),
    PRIMARY KEY(email),
    FOREIGN KEY(email) REFERENCES sailor(email)
    -- Every Sailor must exist either in the table 'senior' or in the table 'junior'
    -- No Junior can exist in the table 'senior'
);

CREATE TABLE country(
    name VARCHAR(70),
    flag VARCHAR(2083) NOT NULL,
    ISO_code VARCHAR(3) NOT NULL,
    PRIMARY KEY(name),
    UNIQUE(ISO_code) -- (IC-5)
    --Every country where boats are registered must have at least one location (IC-1)
);

CREATE TABLE location(
    latitude NUMERIC(8,6),
    longitude NUMERIC(9,6),
    name VARCHAR(80) NOT NULL,
    country_name VARCHAR(70) NOT NULL,
    PRIMARY KEY(latitude, longitude),
    FOREIGN KEY(country_name) REFERENCES country(name)
    -- Any two locations must be at least one nautical mile apart (IC-2)
    --Every country where boats are registered must have at least one location (IC-1)
);

CREATE TABLE boat_class(
    name VARCHAR(80),
    max_length NUMERIC(9,2) NOT NULL,
    PRIMARY KEY(name)
);

CREATE TABLE sailing_certificate(
    sailor_email VARCHAR(254),
    issue_date TIMESTAMP,
    expiry_date DATE NOT NULL,
    for_class_name VARCHAR(80) NOT NULL,
    PRIMARY KEY(sailor_email, issue_date),
    FOREIGN KEY(sailor_email) REFERENCES sailor(email),
    FOREIGN KEY(for_class_name) REFERENCES boat_class(name)
    --Every Sailing Certificate must exist in the table 'valid_for'
);

CREATE TABLE boat(
    country_name VARCHAR(70),
    cin VARCHAR(30),
    boat_name VARCHAR(200) NOT NULL,
    length NUMERIC(9,2) NOT NULL,
    class_name VARCHAR(80) NOT NULL,
    year SMALLINT NOT NULL,
    PRIMARY KEY(country_name, cin),
    FOREIGN KEY(country_name) REFERENCES country(name),
    FOREIGN KEY(class_name) REFERENCES boat_class(name)
    --Every country where boats are registered must have at least one location (IC-1)
);

CREATE TABLE reservation(
    boat_country_name VARCHAR(70),
    boat_cin VARCHAR(30),
    start_date DATE,
    end_date DATE,
    responsible_sailor_email VARCHAR(254) NOT NULL,
    PRIMARY KEY(boat_country_name, boat_cin, start_date, end_date),
    FOREIGN KEY(boat_country_name, boat_cin) REFERENCES boat(country_name, cin),
    FOREIGN KEY(start_date, end_date) REFERENCES date_interval(start_date, end_date),
    FOREIGN KEY(responsible_sailor_email) REFERENCES senior(email)
    --Every reservation must exist in the table 'authorised'
    --One of the senior authorized sailors must be the responsible for the reservation (IC-6)
    --The skipper must be an authorized sailor of the corresponding reservation (IC-3)
);

CREATE TABLE trip(
    boat_country_name VARCHAR(70),
    boat_cin VARCHAR(30),
    start_date DATE,
    end_date DATE,
    take_off DATE,
    arrival DATE NOT NULL,
    insurance VARCHAR(80) NOT NULL,
    from_location_latitude NUMERIC(8,6) NOT NULL,
    from_location_longitude NUMERIC(9,6) NOT NULL,
    to_location_latitude NUMERIC(8,6) NOT NULL,
    to_location_longitude NUMERIC(9,6) NOT NULL,
    skipper_email VARCHAR(254) NOT NULL,
    PRIMARY KEY(boat_country_name, boat_cin, start_date, end_date, take_off),
    FOREIGN KEY(boat_country_name, boat_cin, start_date, end_date) REFERENCES reservation(boat_country_name, boat_cin, start_date, end_date),
    FOREIGN KEY(from_location_latitude, from_location_longitude) REFERENCES location(latitude, longitude),
    FOREIGN KEY(to_location_latitude, to_location_longitude) REFERENCES location(latitude, longitude),
    FOREIGN KEY(skipper_email) REFERENCES sailor(email),
    CHECK (take_off > start_date) -- (IC-4)
    --The skipper must be an authorized sailor of the corresponding reservation (IC-3)
);

CREATE TABLE valid_for(
    sailor_email VARCHAR(254),
    issue_date TIMESTAMP,
    country_name VARCHAR(70),
    PRIMARY KEY(sailor_email, issue_date, country_name),
    FOREIGN KEY(country_name) REFERENCES country(name),
    FOREIGN KEY(sailor_email, issue_date) REFERENCES sailing_certificate(sailor_email, issue_date)
    --Every Sailing Certificate must exist in the table 'valid_for'
);

CREATE TABLE authorised(
    sailor_email VARCHAR(254),
    boat_country_name VARCHAR(70),
    boat_cin VARCHAR(30),
    start_date DATE,
    end_date DATE,
    PRIMARY KEY(boat_country_name, boat_cin, start_date, end_date, sailor_email),
    FOREIGN KEY(boat_country_name, boat_cin, start_date, end_date) REFERENCES reservation(boat_country_name, boat_cin, start_date, end_date),
    FOREIGN KEY(sailor_email) REFERENCES sailor(email)
    --Every reservation must exist in the table 'authorised'
    --One of the senior authorized sailors must be the responsible for the reservation (IC-6)
    --The skipper must be an authorized sailor of the corresponding reservation (IC-3)
);
