-- 2. Integrity Constraints
-- Write the code to implement the following integrity constraints - which are presented assuming your knowledge of previous phases - with the SQL procedural extensions (Stored Procedures, Triggers, and Deferred Constraint checking) in:
-- (IC-1) Every Sailor is either Senior or Junior.
-- (IC-2) The take-off and arrival dates of Trips for the same reservation must not overlap (i.e., one Trip cannot take off before the arrival of another).
-- The integrity constraints definable without resorting to procedural extensions (Stored Procedures and Triggers), should be implemented using other mechanisms if appropriate. However, mechanisms such as ON DELETE CASCADE and ON UPDATE CASCADE are not allowed.

-- (IC-1) Every Sailor is either Senior or Junior.
CREATE OR REPLACE FUNCTION every_sailor_is_either_junior_or_senior() RETURNS TRIGGER AS
$$
BEGIN
IF NOT sailor IN junior OR sailor IN senior THEN
RAISE EXCEPTION '(IC-1) Every Sailor is either Senior or Junior.'
END IF;
RETURN NEW; END;
$$ LANGUAGE plpgsql;

-- (IC-2) The take-off and arrival dates of Trips for the same reservation must not overlap (i.e., one Trip cannot take off before the arrival of another).
CREATE OR REPLACE FUNCTION trips_cannot_overlap() RETURNS TRIGGER AS
$$
BEGIN
IF trip IN interval THEN
RAISE EXCEPTION '(IC-1) Every Sailor is either Senior or Junior.'
END IF;
RETURN NEW; END;
$$ LANGUAGE plpgsql;