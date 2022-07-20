separador = '#' *20
print(separador)
print('Olá Mundo!')
print(separador)

numero = input("Digite um número: ")
print(float(numero))

print(separador)

numero_1 = input('Digite um número: ')
print(f"O mesmo número em formato 'float' será: {float(numero_1)}")
print(f"O mesmo número em formato 'float' será: {int(numero_1)}")

print(separador)

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

result = num1 + num2

print(f'O resultado da soma entre {num1} + {num2} é: {result}')

print(separador)

nota_final = 0
bimestre = 0
for nota_media in range(1, 5):
    nota_aluno = float(input(f'Digite a nota do {nota_media}° bimestre: '))
    bimestre += 1
    nota_final += nota_aluno
print(f'A média de notas foi: {nota_final/bimestre}')

print(separador)

metros = float(input('Digite a medida em metros: '))
centimetros = metros*100
print(f'A medida de {metros}m, convertida em centímetros é: {centimetros:.2f}cm.')

print(separador)

raio = float(input('Digite o raio do círculo: '))
diametro = 3.14 * (raio ** 2)
print(f'O raio fornecido foi: {raio}\n'
      f'O diamêtro do circulo desse raio é equivalente à: {diametro:.3f}')

print(separador)

salario_hora = float(input('Digite o valor referente ao seu salário por hora: R$ '))
horas_trabalho = int(input('Digite quantas horas trabalhadas por dia: '))
salario_mensal = 22 * (salario_hora * horas_trabalho)

print(f'O seu sálario nesse mês foi: R${salario_mensal}')

print(separador)

temperatura_Fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))

celsius = 5 * ((temperatura_Fahrenheit - 32) / 9)
kelvin = celsius - 273

print(f'Temperatura em °F: {temperatura_Fahrenheit}°F\n'
      f'Convertida para Celsius: {celsius:.2f}°C\n'
      f'Convertida para Kelvin: {kelvin:.2f}°K.')

temperatura_Celsius = float(input('Digite a temperatura em Fahrenheit: '))

fahrenheit = (temperatura_Celsius * (9/5)) + 32
kelvin = temperatura_Celsius = 273.15

print(f'Temperatura em Celsius: {temperatura_Celsius}°C\n'
      f'Convertida para Fahrenheit: {fahrenheit:.2f}°F\n'
      f'Convertida para Kelvin: {kelvin:.2f}°K.')

print(separador)

#Forma 1
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano[Com 4 dígitos]: '))

print(f'A data informada foi: {dia}/{mes}/{ano}')

#Forma 2
lista_mes = ['Janeiro', 'Fevereiro', 'Março',
             'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro',
             'Outrubro', 'Novembro', 'Dezembro']

print(f'A data informada foi: {dia}/{lista_mes[int(mes) - 1]}/{ano}')

print(separador)

nome = str(input('Digite seu nome: ')).title()
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso atual: '))
altura = int(input('Digite sua altura em cm: '))/100
alerta = ''
condicao = ''
imc = (peso / (altura * altura))

if imc < 18.5:
    condicao = 'Abaixo do peso'
elif 18.5 <= imc < 25.0:
    condicao = 'Peso Ideal'
elif 25.0 <= imc < 30.0:
    condicao = 'Sobrepeso'
    alerta = 'Recomenda-se um acompanhamento médico.'
elif 30.0 <= imc <= 40:
    condicao = 'Obesidadde'
    alerta = 'Procure seu médico.'
else:
    condicao = 'Obesidade Mórbida'
    alerta = 'Procure seu médico com urgência.'
print(f'{"=" * 20:>}', 'RESULTADOS', f'{"=" * 20:>}')
print(f'Paciente: {nome};\n'
      f'Idade: {idade} anos;\n'
      f'IMC: {imc:.2f} Kg/m²\n'
      f'Condição: {condicao}.\n'
      f'{alerta.upper()}')

print(separador)

salario = float(input('Digite o valor: R$ '))

salario += (salario * 0.15)

print(f'O novo valor é R${salario:.2f}')

print(separador)

salario = float(input('Digite o valor: R$ '))

salario -= (salario * 0.15)

print(f'O novo valor é R${salario:.2f}')

print(separador)

print('='*5, "DESAFIO", '='*5)

print(separador)

vel_inicial = float(input('Digite a velocidade inicial [formato: m/s]: '))
pos_inicial = int(input('Digite a posição inicial [formato: m]: '))
inst_tempo = int(input('Digite o tempo [formato: s]: '))
acel_gravit = -10

yt = pos_inicial + (vel_inicial * inst_tempo) + ((1/2)*((acel_gravit * inst_tempo)**2))

print(f'A posição do projétil no instante {inst_tempo}s é: {yt}m')

print(separador)

import datetime
relogio = input('Você deseja saber a hora [S/N]? ').split()
data = datetime.date.today().strftime('%d/%m/%Y')
hora = datetime.datetime.now().time().strftime('%H:%M:%S')
if relogio[0] == 'S':
    print(f'A data de hoje é: {data}\n'
          f'A hora atual é: {hora}')
elif relogio[0] == 'N':
    print('Obrigado, tenha um ótimo dia!')
else:
    print('Comando Inválido!')

print(separador)
