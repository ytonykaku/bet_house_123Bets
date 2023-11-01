-- QUERIES DA MADRUGADA
SELECT *
FROM (SELECT *
      FROM (SELECT *
            FROM (SELECT *
                  FROM Bet b INNER JOIN Fighter f ON b.fA = f.name) tmpA
            INNER JOIN Fighter f ON tmpA.fB = f.name) tmpB
      INNER JOIN Fighter f ON tmpB.winner = f.name) tmpW
INNER JOIN Fight f ON tmpW.fA = f.fA AND tmpW.fB = f.fB
WHERE tmpW.owner = ?;
