UPDATE
User
SET
utype = 1
WHERE
cpf = {cpf};

INSERT OR IGNORE INTO Admin(uid)
            SELECT uid FROM User WHERE cpf = {cpf};

DELETE FROM
Punter
WHERE
    uid = (SELECT uid
           FROM User
           WHERE cpf = {cpf});
