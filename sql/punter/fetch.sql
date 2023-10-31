select
u.name, u.login, u.password, u.cpf, u.email, u.utype, t.profit, t.loss, t.available, t.applied
from
    (select
     *
     from
     Punter p inner join Wallet w
     on
     p.cpf = w.cpf_owner) t
inner join User u
on
t.cpf = u.cpf;