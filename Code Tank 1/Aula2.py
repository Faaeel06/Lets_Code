genero = ' '
sexo = str(input('Digite o sexo[M/F/I]: '))

if sexo == 'M' or 'm':
    genero = 'Masculino'
elif sexo == 'F' or 'f':
    genero = 'Feminino'
elif sexo == 'I' or 'i':
    genero = 'Intersexo'
else:
    genero = 'Inválido'

print(f'Sexo: {genero}')