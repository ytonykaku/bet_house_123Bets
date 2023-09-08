SELECT
Punter.id, Punter.name, Punter.cpf, Punter.profit, Punter.loss,
Wallet.id, Wallet.value_available, Wallet.value_applied
FROM
Punter
INNER JOIN
Wallet
ON
Punter.wallet = Wallet.id
WHERE
Punter.id = ?;

