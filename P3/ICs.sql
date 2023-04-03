----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- IC-1: Every sailor is either senior or junior
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- trigger activated when inserting/updating on sailor: mandatory constraint and disjoint constraint
CREATE OR REPLACE FUNCTION check_sailor_mandatory_senior_junior_insert_update()
    RETURNS TRIGGER AS
$$
BEGIN
    --check mandatory constraint
    IF NEW.email NOT IN ((SELECT email FROM junior) UNION (SELECT email FROM senior)) THEN
        RAISE EXCEPTION 'The sailor whose email is % must be in table Senior or Junior.', new.email;
    END IF;

    --check disjoint
    IF NEW.email IN ((SELECT email FROM junior) INTERSECT (SELECT email FROM senior)) THEN
        RAISE EXCEPTION 'The sailor whose email is % can not be in table Senior and Junior at the same time.', new.email;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tg_check_sailor_mandatory_senior_junior_insert_update ON sailor;

CREATE CONSTRAINT TRIGGER tg_check_sailor_mandatory_senior_junior_insert_update
AFTER INSERT OR UPDATE ON sailor DEFERRABLE INITIALLY DEFERRED
FOR EACH ROW EXECUTE PROCEDURE 
check_sailor_mandatory_senior_junior_insert_update();


-- trigger activated when inserting/updating on senior and junior: disjoint constraint 
CREATE OR REPLACE FUNCTION check_disjoint_senior_junior()
    RETURNS TRIGGER AS
$$
BEGIN
    --check disjoint
    IF NEW.email IN ((SELECT email FROM junior) INTERSECT (SELECT email FROM senior)) THEN
        RAISE EXCEPTION 'The sailor whose email is % can not be in table Senior and Junior at the same time.', new.email;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tg_check_if_senior_is_junior ON senior;
DROP TRIGGER IF EXISTS tg_check_if_junior_is_senior ON junior;

CREATE TRIGGER tg_check_if_senior_is_junior
AFTER INSERT OR UPDATE ON senior
FOR EACH ROW EXECUTE PROCEDURE 
check_disjoint_senior_junior();

CREATE TRIGGER tg_check_if_junior_is_senior
AFTER INSERT OR UPDATE ON junior
FOR EACH ROW EXECUTE PROCEDURE 
check_disjoint_senior_junior();


-- trigger activated when deleting on senior/junior
CREATE OR REPLACE FUNCTION delete_on_sailor()
    RETURNS TRIGGER AS
$$
BEGIN
    DELETE FROM sailor
    WHERE sailor.email = OLD.email;

    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tg_delete_on_sailor_senior ON senior;
DROP TRIGGER IF EXISTS tg_delete_on_sailor_junior ON junior;

CREATE CONSTRAINT TRIGGER tg_delete_on_sailor_senior
AFTER DELETE ON senior
FOR EACH ROW EXECUTE PROCEDURE delete_on_sailor();

CREATE CONSTRAINT TRIGGER tg_delete_on_sailor_junior
AFTER DELETE ON junior
FOR EACH ROW EXECUTE PROCEDURE delete_on_sailor();


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- IC-2: The take-off and arrival dates of trips for the same reservation must not overlap 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- trigger activated when inserting/updating on trip
CREATE OR REPLACE FUNCTION check_trip_not_overlap()
    RETURNS TRIGGER AS
$$
BEGIN
    IF (NEW.takeoff < NEW.reservation_start_date) THEN
        RAISE EXCEPTION 'The takeoff of a trip must not be earlier than the start date of the corresponding reservation.';
    END IF;

    IF (NEW.arrival > NEW.reservation_end_date) THEN
        RAISE EXCEPTION 'The arrival of a trip must not be later than the end date of the corresponding reservation.';
    END IF;

    IF (NEW.takeoff > NEW.arrival) THEN
        RAISE EXCEPTION 'The takeoff date of a trip must not be later than its arrival date!';
    END IF;

    IF(
        (NEW.takeoff < ANY(
            SELECT takeoff
            FROM trip 
            WHERE trip.reservation_start_date = NEW.reservation_start_date AND trip.reservation_end_date = NEW.reservation_end_date AND trip.boat_country = NEW.boat_country AND trip.cni = NEW.cni
        )
        AND
        NEW.arrival > ANY(
            SELECT takeoff
            FROM trip 
            WHERE trip.reservation_start_date = NEW.reservation_start_date AND trip.reservation_end_date = NEW.reservation_end_date AND trip.boat_country = NEW.boat_country AND trip.cni = NEW.cni 
            AND trip.takeoff > NEW.takeoff
        ))
        OR
        (NEW.takeoff > ANY(
            SELECT takeoff
            FROM trip 
            WHERE trip.reservation_start_date = NEW.reservation_start_date AND trip.reservation_end_date = NEW.reservation_end_date AND trip.boat_country = NEW.boat_country AND trip.cni = NEW.cni
        )
        AND
        NEW.takeoff < ANY(
            SELECT arrival
            FROM trip 
            WHERE trip.reservation_start_date = NEW.reservation_start_date AND trip.reservation_end_date = NEW.reservation_end_date AND trip.boat_country = NEW.boat_country AND trip.cni = NEW.cni 
            AND trip.takeoff < NEW.takeoff
        ))
    ) 
    THEN
        RAISE EXCEPTION 'Trips must not overlap!';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tg_check_trip_not_overlap ON trip;
CREATE TRIGGER tg_check_trip_not_overlap
BEFORE INSERT OR UPDATE ON trip
FOR EACH ROW EXECUTE PROCEDURE check_trip_not_overlap();
