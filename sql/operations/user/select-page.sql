SELECT
name, login, cpf, email, utype
FROM
User
LIMIT
:num_items
OFFSET
(:page_num - 1) * :num_items;
