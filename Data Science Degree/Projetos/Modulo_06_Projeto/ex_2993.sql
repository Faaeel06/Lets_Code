CREATE TABLE value_table (
    amount integer
);

--GRANT SELECT ON value_table TO sql_user;

insert into
value_table (amount)
values
(4),(6),(7),(1),(1),(2),(3),(2),(3),(1),(5),(6),(1),(7),(8),(9),(10),(11),(12),(4),(5),(5),(3),(6),(2),(2),(1);

SELECT amount 
FROM value_table 
GROUP BY amount 
ORDER BY count(amount) DESC
LIMIT 1