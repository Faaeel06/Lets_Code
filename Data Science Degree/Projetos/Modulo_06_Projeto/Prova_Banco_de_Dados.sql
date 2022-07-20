CREATE TABLE customers (
  id NUMERIC PRIMARY KEY,
  name CHARACTER VARYING (255),
  street CHARACTER VARYING (255),
  city CHARACTER VARYING (255),
  state CHAR (2),
  credit_limit NUMERIC
);

INSERT INTO customers (id, name, street, city, state, credit_limit)
VALUES
  (1,	'Pedro Augusto da Rocha',	'Rua Pedro Carlos Hoffman',	'Porto Alegre',	'RS',	700.00),
  (2,	'Antonio Carlos Mamel',	'Av. Pinheiros',	'Belo Horizonte',	'MG',	3500.50),	
  (3,	'Luiza Augusta Mhor,',	'Rua Salto Grande',	'Niteroi',	'RJ',	4000.00),
  (4,	'Jane Ester',	'Av 7 de setembro',	'Erechim',	'RS',	800.00),
  (5,	'Marcos Antônio dos Santos',	'Av Farrapos',	'Porto Alegre',	'RS',	4250.25);

/* BLOCO 1 - 
A) para criação da tabela eu defini
as colunas e suas variáveis que podem
ser aceito a insersão de dados, a fim
de gerar maior eficiência na tabela e
diminuir divergências nos dados;

B) Para a coluna 'CPF do cliente' será melhor definido
o tipo de dado CHAR com limitação de carateres inseridos.
	Para coluna 'Opinião do cliente' será interesante trabalhar
com tipo de dado TEXT para compreender toda a dimensão de variedade
e tamanho do dado inserido.
	Para a coluna 'Data e Hora da compra' existem dois modos;
TIMESTAMP e DATETIME, onde o primeiro ocupa menor espaço de memória
mas o segundo insere o formato UTC.

C) Vendo que o campo é o ID eu sugeriria manter o tipo de dado INTEGER,
pois o mesmo aloca menor espaço de memória sem gerar impacto direto no tratamento
do dado, mas caso seja necessário alterar eu usaria o comando ""*/

CREATE TABLE providers (
  id numeric PRIMARY KEY,
  name varchar(50),
  street varchar(50),
  city varchar(50),
  state varchar(2)
);

INSERT INTO providers (id, name, street, city, state)
VALUES 
  (1,	'Henrique',	'Av Brasil',	'Rio de Janeiro',	'RJ'),
  (2,	'Marcelo Augusto',	'Rua Imigrantes',	'Belo Horizonte',	'MG'),
  (3,	'Caroline Silva',	'Av São Paulo',	'Salvador',	'BA'),
  (4,	'Guilerme Staff',	'Rua Central',	'Porto Alegre',	'RS'),
  (5,	'Isabela Moraes',	'Av Juiz Grande',	'Curitiba',	'PR'),
  (6,	'Francisco Accerr',	'Av Paulista',	'São Paulo',	'SP');
  
  
 /* BLOCO 2 - 
 1) Não é recomendado chamar levianamente todos os dados de  uma tabela,
 devido a densidade da mesma e a capacidade da máquina usada na operação,
 é sempre importante ser objetivo na abordagem, então eu não faria tal recomendação.
 
 2) Contagem do número de linhas na coluna a fim de retornar um valor numérico exato,
 que ajuda a explicitar a densidade da tabela.
 
 3)SELECT DISTINXT(state) FROM providers;
 
 4)SELECT
	STATE,
	COUNT(*) AS QTD
FROM providers
GROUP BY state
HAVING COUNT(*) >= 1;
	a) O GROUP BY irá agrupar todas as ocorrências,
	para gerar um novo filtro após o COUNT.
	b) Trabalhar melhor o filtro e excluir posíveis valores.
	c) HAVING é usado para especificar uma condição de
	pesquisa para um grupo ou um agregado. Já o WHERE
	é usado em conjunto com o FROM para filtrar as linhas
	retornadas do SELECT.*/
 
CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR (100) NOT NULL
);

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR (100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');
	
/* BLOCO 3 - 
1) O JOIN execulta no banco de dados a função de unir duas tabelas
através de uma Primary_Key(PK) e uma Foreign_Key(FK) que devem coincidir
nas duas tabelas.

2) O INNER E LEFT, ambos agregadores do JOIN, respectivamente
exibem valores correspondentes em ambas as tabelas ou exibe todos os
valores da tabela a ser inserido os dados correspondentes a tabela a ser
chamada, completando com 'NULL' os dados vazios.

3) Pesquisa realizada atráves do link(https://stackoverflow.com/questions/36872053/update-a-single-column-on-multiple-rows-with-one-sql-query)
UPDATE basket_b
SET    fruit_b = 
       CASE fruit_b
            WHEN 'Orange' THEN 'Laranja'
            WHEN 'Apple' THEN 'Maçã'
            WHEN 'Watermelon' THEN 'Melancia'
            WHEN 'Pear' THEN 'Pêra'
       END
WHERE  fruit_b IN ('Orange', 'Apple', 'Watermelon', 'Pear');

Utilizando o comando UPDATE é possível alterar valores da coluna,
foi usado para fazer a tradução da coluna 'basket_b' onde o comando
'WHEN' descreve a condição que deve ser alterada.

4) o comando 'WHERE' descreve a condição de alteração que deve ser passada para a tabela,
caso não seja especificado, todos os valores na coluna serão modificados.*/

/* Prova feita com auxílio do Dan, Gabi e Jere grandes colegas que me ajudaram na compreensão do desafio.*/