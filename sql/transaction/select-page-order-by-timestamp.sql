SELECT
id, ttype, value, timestamp
FROM
PTransaction
WHERE
pid = :punter_id
ORDER BY
timestamp
LIMIT
:num_items
OFFSET
(:page_num - 1) * :num_items;
