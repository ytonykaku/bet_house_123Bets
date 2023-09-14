SELECT
id, ttype, value, timestamp
FROM
PTransaction
WHERE
pid = :punter_id
ORDER BY
timestamp;
