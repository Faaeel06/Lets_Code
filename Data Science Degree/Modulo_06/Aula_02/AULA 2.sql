/*Criando nosso primeiro servidor no PGADMIN:
      Criando nosso servidor no PGADMIN (SGBD):
                "Botao direito em Server > Create > Server..."
                Em General:
                    Name: Modulo5
                Em Connection:
                    HOSTNAME/ADDRESS: localhost
                    Password: sua senha master*/


/*      
Vamos criar o nosso primiro banco de dados (material)
 
     "Botão direito Databases > Create Database"
    Em General:
        DatabaseName = aul
        Owner= postgres
    Definition:
        Encoding UTF8

    Ao criar o database, podemos ver a definição por linha de código na Aba SQL;*/

  
  
    /* Query ou consulta é como chamamos os nossos comandos no sql*/



/* Create database */

    --documentação: https://www.postgresql.org/docs/9.0/sql-createdatabase.html
    -- exemplo 1:
        CREATE DATABASE "Aula"
        WITH 
        OWNER = postgres
        ENCODING = 'UTF8'
        LC_COLLATE = 'Portuguese_Brazil.1252'
        LC_CTYPE = 'Portuguese_Brazil.1252'
        TABLESPACE = pg_default
        CONNECTION LIMIT = -1;
    -- exemplo 2:
        CREATE DATABASE aula_2;

/* Drop database*/

--Documentação: https://www.postgresql.org/docs/9.0/sql-dropdatabase.html

    --exemplo 1: 
        DROP DATABASE [ IF EXISTS ] name
    --Exemplo 2:]
        DROP DATABASE [ IF EXISTS ] aula_2;
-- Cuidado, não execute esse comando no seu trabalho, sem ter certeza que deseja fazer isso!


/*Criar novas tabelas*/

   CREATE TABLE aluno(
      nome VARCHAR(255),
        cpf CHAR(11),
        observacao TEXT,
        idade INTEGER,
        dinheiro NUMERIC(10,2),
        altura REAL,
        ativo BOOLEAN,
        data_nascimento DATE,
        hora_aula TIME,
        matriculado_em TIMESTAMP
    );  
    /* cada campo tem um tipo de dado, checar na documentação:https://www.postgresql.org/docs/9.5/datatype.html Os principais são NUMERICOS,TEXTOS,DATAS e BOOLEANO*/


/*Inserindo dados na tabela*/

    INSERT INTO aluno (
        nome,
        cpf,
        observacao,
        idade,
        dinheiro,
        altura,
        ativo,
        data_nascimento,
        hora_aula,
        matriculado_em
    ) VALUES (
        'Matheus',
        '1234568911',
        'gosto muito de voces',
        25,
        2,00,
        1.81,
        TRUE,
        '1996-04-23',
        '19:00:00',
        '2020-02-08 12:32:45'
    );

    /* cada campo tem um tipo de dado, checar na documentação:https://www.postgresql.org/docs/9.5/datatype.html Os principais são NUMERICOS,TEXTOS,DATAS e BOOLEANO*/


/*SELECIONANDO DADOS DE UMA TABELA*/

SELECT 1
SELECT 1+1
SELECT "HELLO WORLD"
OU 

SELECT 1 AS CAMPO_1
SELECT 1+1 AS CAMPO_SOMA 
SELECT "HELLO WORLD" AS MENSAGEM

-- da tabela aluno:

SELECT * FROM aluno; -- o parametro * siginifica todos os campos 
SELECT CPF,ALTURA FROM ALUNO;
SELECT matriculado_em AS DATA_DA_MATRICULA, CPF AS RG, ALTURA FROM ALUNO; -- altera somente no resultado da query, é apenas uma consulta, nao altera a tabela aluno.
SELECT CPF,ALTURA +12 as altura_somada_12 FROM ALUNO;

-- quantidade de linhas de uma tabela

SELECT COUNT(*) FROM aluno;



/* FILTROS WHERE */

SELECT * FROM customers where country in ('BRAZIL','Argentina','Alemanha')


/*exemplo de operadores*/
/*
=	Equal	
>	Greater than	
<	Less than	
>=	Greater than or equal	
<=	Less than or equal	
<>	Not equal. =	
BETWEEN	Between a certain range	
LIKE	Search for a pattern	
IN	To specify multiple possible values for a column*/ 



/*INSTALAR DATABASE NORTHWIND*/
https://github.com/pthom/northwind_psql/blob/master/northwind.sql

-- SÓ RODAR ISSO NO PGADMIN4.






