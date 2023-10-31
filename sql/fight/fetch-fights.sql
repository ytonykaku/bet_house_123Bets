SELECT
temp.fA, temp.oddA, temp.category, temp.nationality, temp.height, temp.n_wins, temp.n_loss,
temp.fB, temp.oddB, final.category, final.nationality, final.height, final.n_wins, final.n_loss,
winner
FROM (SELECT * FROM Fight INNER JOIN Fighter ON fight.fA=fighter.name) temp
INNER JOIN fighter final ON temp.fB=final.name WHERE winner IS NULL;