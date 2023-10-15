SELECT
id, name, login, cpf, email, utype
FROM
User
WHERE
cpf=:cpf;
