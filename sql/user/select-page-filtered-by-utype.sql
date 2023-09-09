SELECT
name, login, cpf, email, utype
FROM
User
WHERE
utype = :selected_utype
LIMIT
:num_items
OFFSET
(:page_num - 1) * :num_items;
