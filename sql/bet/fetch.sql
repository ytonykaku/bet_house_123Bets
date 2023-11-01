SELECT *
FROM (SELECT *
      FROM (SELECT *
            FROM (SELECT *
                  FROM Bet b
                  INNER JOIN Fight f
                  ON b.fight_name = f.name) bf
            INNER JOIN Fighter fg
            ON fg.name = bf.fA) bfa
      INNER JOIN Fighter fg
      ON fg.name = bfa.fB) bfafb
INNER JOIN Fighter fg
ON fg.name = bfafb.winner
WHERE bfafb.owner = ?;
