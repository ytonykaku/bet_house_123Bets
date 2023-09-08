UPDATE
User
SET
utype = 1
WHERE
cpf = {cpf};

INSERT INTO Admin(uid)
            SELECT id FROM User WHERE cpf = {cpf};

DELETE FROM
Punter
WHERE
uid = (SELECT id
       FROM User
       WHERE cpf = {cpf});
