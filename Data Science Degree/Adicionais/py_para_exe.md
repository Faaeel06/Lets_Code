# Criando programas executáveis (.exe)

Imagine que você deseja enviar um programa que você fez em Python para um amigo. Para que seu amigo consiga executar seu programa, é necessário que ele também tenha o Python instalado no computador dele -- ele teria que fazer todo aquele processo de instalação do Python que fizemos na primeira aula do curso.

Muitas vezes, isso é bastante inconveniente -- não seria bem melhor se seu amigo pudesse executar seu programa feito em Python independentemente dele ter o Python instalado no computador dele?

A boa notícia é que isso é possível! Basta nós transformarmos o nosso programa Python (de extensão ".py") para um programa executável (de extensão ".exe"), que funciona independente de qualquer instalação do Python!

Há diversas formas de fazer isso, mas veremos aqui a forma mais simples, que é utilizando a biblioteca **pyinstaler**! Para acessar a documentação da biblioteca, [clique aqui!](https://www.pyinstaller.org/index.html)


De maneira simplificada, o que a biblioteca faz é comprimir o código Python (arquivo .py) juntamente com todas as bibliotecas utilizadas nele, e criar versões locais das bibliotecas e do próprio Python, sem a necessidade que estes sejam instalados. Com isso, é criado um arquivo executável (.exe), que ao ser executado é interpretado localmente, fazendo referência às pastas locais com as bibliotecas -- e assim o programa é executado, independente do Python ou as bibliotecas estarem instaladas no computador! Bem legal, né?

Agora que entendemos o funcionamento básico da biblioteca, vamos ver como utiliá-la! Basta seguir o passo-a-passo a seguir:

___________________________


- 1) Caso você esteja usando o Jupyter Notebook, é necessário salvar o código do notebook que queremos transformar em .exe como um arquivo ".py":
	- Pra fazer isso, abra o Notebook, e no menu superior vá em em File >> Download as >> Python (.py);
	- Se você usa alguma IDE e já tem o arquivo .py diretamente, pode ir pro passo seguinte!

- 2) Crie uma pasta nova e coloque o arquivo .py nesta pasta
	- Dê o nome que desejar à pasta -- é nela que ficará o arquivo .exe final e todas as outras pastas de referência às bibliotecas, como mencionamos acima;
	- Crie a pasta em um local simples (como, por exemplo, dentro da pasta "Documentos"), pois teremos que "navegar" até essa pasta no passo 4), abaixo.

- 3) Caso você ainda não tenha instalado, é necessário instalar o pyinstaller (Isso é feito apenas uma vez!)
	- A instalação é feita como você instalaria qualquer biblioteca:
		- Abra o terminal (Linux ou Mac), Prompt de comando ou Anaconda Prompt (Windows), digite ```pip install pyinstaller```, e dê enter;
		- Pra quem tem o anaconda, pode usar também o ```conda install pyinstaller```;
		- Também é possível instalar diretamente pelo Jupyter, executando em uma célula o código ```!pip install pyinstaller```.


- 4) Uma vez instalada a biblioteca, você deve utilizar o terminal/prompt de comando pra navegar até a pasta criada no passo 2):
	- Para fazer isso, utilize o comando ```"cd"``` no terminal/prompt para mudar de pastas, até você chegar na pasta desejada.

- 5) Quando você estiver na pasta, rode no terminal/prompt o seguinte comando: ```pyinstaller nome_do_programa.py```
	- Vai aparecer um monte de código na tela do prompt, normal. Isso é a biblioteca em ação!
	- Quando o processo terminar, aparecerá uma mensagem de sucesso no prompt. Depois disso, pode fecha-lo.

- 6) Agora vá até a pasta do passo 2), e veja que uma pasta chamada "dist" foi criada. 
	- Pode ser que outras pastas também tenham sido criadas -- essas são as passas com as bibliotecas e outros arquivos importantes pro seu arquivo .exe funcionar, que mencionamos antes.

- 7) Dentro desta pasta "dist" você vai encontrar o arquivo .exe! Pronto!


___________________________

Pronto! Seguindo o passo-a-passo acima, você conseguiu criar um arquivo executável capaz de rodar em qualquer computador, independente da instalção do Python!

> Obs.: uma vez instalada a biblioteca, o passo 3) não precisará mais ser repetido! Lembre-se que só é necessário instalar as bibliotecas uma vez!

Um ponto importante é que todos os arquivos nas pastas criadas além da "dist" são necessários pro seu arquivo .exe ser executado corretamente! Então, pra você enviar o programa pro seu amigo, é necessário enviar também todas essas pastas.

> A dica é: comprima a pasta criada no passo 2) (ou seja, crie um arquivo .zip ou .rar), e envie este arquivo comprimido! Assim, você garante que todos os arquivos necessários serão também enviados!

Feito isso, o que importa é que seu arquivo .exe foi criado! Você pode criar um atalho pra ele e colocá-lo em qualquer outra pasta, ou seja, não é necessário entrar na pasta do passo 2) sempre que você for querer exectuar o programa!

Vamos a um exemplo?


Considere o programa a seguir:

```python
import datetime as dt

nome = input("\nQual é o seu nome? ")

print("\nBom dia," + nome + "!")

print("\nEu sou um programa pra te falar qual é a data e hora atuais!")

print("\nO dia de hoje é:", dt.datetime.strftime(dt.datetime.now(), "%d/%m/%Y"))

print("\nE a hora atual é:", dt.datetime.strftime(dt.datetime.now(), "%H:%M:%S"))

resposta = input("\nVocê deseja fechar o programa? (s/n) ")

while resposta.lower() != "s":

	resposta = input("\nVocê deseja fechar o programa? (s/n) ")

```

É um programa bem simples, que pede o nome do usuário, depois exibe o dia e hora atuais (para isso, utiliza a biblioteca datatime). Por fim, pede a confirmação do usuário para fechar o programa.

Copie o código acima em um arquivo .py e siga o passo-a-passo acima a partir do passo 2), ou copie o código em um Notebook, e siga a partir do passo 1). Após o passo 7), você terá criado um arquivo .exe do programa acima! Dando dois cliques no arquivo exectuável, você verá o programa acima ser executado no terminal/prompt de comando! E caso você faça uma interface gráfica, é a interface que será aberta ao executar o arquivo .exe!

Agora você consegue enviar seus programas a quem quiser! Muito bem!