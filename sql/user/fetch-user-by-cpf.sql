SELECT
uid, name, login, cpf, email, utype
FROM
User
WHERE
cpf=:cpf;
