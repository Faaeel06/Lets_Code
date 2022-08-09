--Aula de integração com python

-- Online Transacional Processing
-- Pessoas --> Sapiens//Aplicação(Iot, API, ERPs) --> BOX|OLTP (SQL server)| & BOX|Excel| && BOX|Json| & BOX|CSV| & BOX|Sharepoint| --> //BOX|ETL|// --> BOX|Data Warehouse(OLAP)| --> BI (Buisness Inteligence)

--OLTP -> Online Trabsacional PRocessing, bancos transacionais
--OLAP -> Online Analytical Processing, data warehouse, cognos, redshift, synapse

--//ETL// Extrair, Transformar, L(load) carregar
--//ELT// -> Extrair, Carregar, Transformar

--BOX| OLTP |--> ETLs --> BOX|Data Lake| --> ETLs --> BOX| OLAP (DataWarehouse)|
--OLTP

SELECT * FROM city

SELECT * FROM rental

Normalizado --> OLTPs, são normalizados para evitar redundâncias
,Desnormaliza --> OLAPs, possui redundância para ganhar na consulta

SELECT * FROM city

SELECT * FROM actor

INSERT INTO actor_id (actor_id, first_name, last_name)
VALUES (1005, 'Rafael', 'Machado', now())

INSERT INTO actor (first_name, last_name)
VALUES ('Emanuelle', 'Souza')

