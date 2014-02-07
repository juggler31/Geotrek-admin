DROP VIEW IF EXISTS a_v_amenagement;
CREATE VIEW a_v_amenagement AS (
	SELECT e.geom, t.*
	FROM a_t_amenagement AS t, a_b_amenagement AS b, e_t_evenement AS e
	WHERE t.evenement = e.id AND t.type = b.id AND b.type = 'A'
	AND e.supprime = FALSE
);

DROP VIEW IF EXISTS a_v_equipement;
CREATE VIEW a_v_equipement AS (
	SELECT e.geom, t.*
	FROM a_t_amenagement AS t, a_b_amenagement AS b, e_t_evenement AS e
	WHERE t.evenement = e.id AND t.type = b.id AND b.type = 'E'
	AND e.supprime = FALSE
);

DROP VIEW IF EXISTS a_v_signaletique;
CREATE VIEW a_v_signaletique AS (
	SELECT e.geom, t.*
	FROM a_t_amenagement AS t, a_b_amenagement AS b, e_t_evenement AS e
	WHERE t.evenement = e.id AND t.type = b.id AND b.type = 'S'
	AND e.supprime = FALSE
);