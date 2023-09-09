UPDATE
User
SET
utype = 0
WHERE
cpf = {cpf};

INSERT INTO Punter(uid)
            SELECT id FROM User WHERE cpf = {cpf};

INSERT INTO Wallet(pid)
            SELECT id FROM User WHERE cpf = {cpf};

DELETE FROM
Admin
WHERE
uid = (SELECT
       id
       FROM
       User
       WHERE
       cpf = {cpf});
