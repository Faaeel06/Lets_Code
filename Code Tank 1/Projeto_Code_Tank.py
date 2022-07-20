dia = range(1, 32)
mes = range(1, 13)
ano = range(1, 9999)
hora = range(0, 24)
minuto = range(0, 60)
separador = '-=-' * 15
lista_comandos_iniciais = ['Registrar uma vacinação.', 'Adicionar estoque de uma vacina.', 'Controle de Estoque.']

lista_vacinas = [' ', 'Pfizer', 'CoronaVac', 'Astrazeneca']
estoque_vacina = []
estoque_geral = [[], [], []]
cadastro = []
registro_vacinacao = 'SIM'
print(separador)
print(f'{"*" * 10:^5} BEM-VINDA(O) {"*" * 10:^5}')
print(f'{separador}\n'
      f'1 - {lista_comandos_iniciais[0]}\n'
      f'2 - {lista_comandos_iniciais[1]}\n'
      f'3 - {lista_comandos_iniciais[2]}\n'
      f'0 - Encerra o Programa.\n'
      f'{separador}')

comando_inicial = int(input('Digite o comando que deseja execultar: '))
while comando_inicial != 0:
    if comando_inicial == 1:
        print(separador)
        print(f'{"*" * 10:^5} CADASTRO DE VACINAÇÃO {"*" * 10:^5}')
        # Registrar uma vacinação.

        while registro_vacinacao[0] == 'S':
            registro_vacinacao = str(input('Deseja registrar vacinação. [S/N]: ')).upper()
            if registro_vacinacao[0] == 'S':
                print(f'{" " * 5:^5}Registrar Vacinação {" " * 5:^5}')
                nome_usuario = str(input('Nome paciente: ')).title()
                print(f'1 - {lista_vacinas[1]}\n'
                      f'2 - {lista_vacinas[2]}\n'
                      f'3 - {lista_vacinas[3]}')

                validado_vacina = ''
                tipo_vacina = int(input('Digite a opção de vacina: '))
                while validado_vacina != 'SIM':
                    if tipo_vacina in range(1, 4):
                        validado_vacina = 'SIM'
                    elif tipo_vacina != range(1, 3):
                        validado_vacina = 'NÃO'
                        print('Opção de vacina inválida. Tente novamente.')
                        tipo_vacina = int(input('Digite a opção de vacina: '))
                    else:
                        break

                validado_data = ''

                data_vacina = input('Digite a data, somente números: ')
                while validado_data != 'SIM':
                    confere_data = data_vacina.strip()
                    if len(confere_data) == 8 and int(confere_data[:2]) in dia and int(
                            confere_data[2:4]) in mes and int(confere_data[4:]) in ano:
                        validado_data = 'SIM'
                    elif len(confere_data) != 8 or confere_data[:2] not in dia and confere_data[2:4] not in mes and int(
                            confere_data[4:]) in ano:
                        validado_data = 'NÃO'
                        print('Opção de vacina inválida. Tente novamente.')
                        data_vacina = input('Digite a data, somente números: ')
                    else:
                        break

                validado_hora = ''

                hora_vacina = input('Digite o horário, somente números: ')
                while validado_hora != 'SIM':
                    confere_hora = hora_vacina.strip()
                    if len(confere_hora) == 4 and int(confere_hora[:2]) in hora and int(confere_hora[2:]) in minuto:
                        validado_hora = 'SIM'
                        print(f'{hora_vacina[:2]}:{hora_vacina[2:]}')
                    elif len(confere_hora) != 4 or int(confere_hora[:2]) not in hora and int(
                            confere_hora[2:4]) not in minuto:
                        validado_hora = 'NÃO'
                        print('Opção de vacina inválida. Tente novamente.')
                        hora_vacina = input('Digite o horário, somente números: ')
                    else:
                        break
                dados_usuario = (f'NOME: {nome_usuario};',
                                 f'VACINA: {lista_vacinas[tipo_vacina]};',
                                 f'DATA: {data_vacina[0:2]}/{data_vacina[2:4]}/{data_vacina[4:]};',
                                 f'HORA: {hora_vacina[0:2]}:{hora_vacina[2:4]}.')
                cadastro.append(dados_usuario)
                estoque_vacina.append(lista_vacinas[tipo_vacina])

            else:
                break

        print(separador * 2)
        print(f'Quantidade de Vacinados: {len(cadastro)}')
        print(f'Quantidade de Vacinas: {len(estoque_vacina)}')

        print(f'{separador}\n'
              f'1 - {lista_comandos_iniciais[0]}\n'
              f'2 - {lista_comandos_iniciais[1]}\n'
              f'3 - {lista_comandos_iniciais[2]}\n'
              f'0 - Encerra o Programa.\n'
              f'{separador}')
        comando_inicial = int(input('Digite o comando que deseja execultar: '))
    elif comando_inicial == 2:
        print(separador)
        print(f'{"*" * 10:^5} CADASTRO DE ESTOQUE {"*" * 10:^5}')
        # Adicionar estoque de uma vacina.
        lista_vacinas = [' ', 'Pfizer', 'CoronaVac', 'Astrazeneca']
        print(f'1 - {lista_vacinas[1]}\n'
              f'2 - {lista_vacinas[2]}\n'
              f'3 - {lista_vacinas[3]}\n'
              f'0 - Digite zero para encerrar.')

        cad_tipo_vacina = int(input('Digite qual tipo deseja adicionar estoque: '))
        while cad_tipo_vacina != 0:
            if cad_tipo_vacina == 1:
                print(f'{lista_vacinas[1].upper()}')
                qtd_tipo_vacina = int(input('Digite a quantidade a ser adicionada ao estoque: '))
                estoque_geral[0].append(qtd_tipo_vacina)
                cad_tipo_vacina = int(input('Digite qual tipo deseja adicionar estoque: '))
            elif cad_tipo_vacina == 2:
                print(f'{lista_vacinas[2].upper()}')
                qtd_tipo_vacina = int(input('Digite a quantidade a ser adicionada ao estoque: '))
                estoque_geral[1].append(qtd_tipo_vacina)
                cad_tipo_vacina = int(input('Digite qual tipo deseja adicionar estoque: '))
            elif cad_tipo_vacina == 3:
                print(f'{lista_vacinas[3].upper()}')
                qtd_tipo_vacina = int(input('Digite a quantidade a ser adicionada ao estoque: '))
                estoque_geral[2].append(qtd_tipo_vacina)
                cad_tipo_vacina = int(input('Digite qual tipo deseja adicionar estoque: '))
            elif cad_tipo_vacina == 0:
                break
            else:
                print('Comando inválido, tente novamente.')
                cad_tipo_vacina = int(input('Digite qual tipo deseja adicionar estoque: '))

        print(f"{lista_vacinas[1]}: {sum(estoque_geral[0])}\n"
              f"{lista_vacinas[2]}: {sum(estoque_geral[1])}\n"
              f"{lista_vacinas[3]}: {sum(estoque_geral[2])}\n")

        print(separador)
        print(f'Quantidade de Vacinados: {len(cadastro)}')
        print(f'Média diária de vacinados: {len(cadastro) / 30}')
        print(separador)

        media_por_vacina = 0
        for analise_vacinados in range(1, 4):
            if len(estoque_vacina) != 0:
                media_por_vacina = estoque_vacina.count(lista_vacinas[analise_vacinados]) / len(estoque_vacina)

            elif len(estoque_vacina) == 0:
                print(f'{media_por_vacina}')
            print(separador)
            print(f'Vacinados com {lista_vacinas[analise_vacinados]}:'
                  f'{estoque_vacina.count(lista_vacinas[analise_vacinados])}')
            print(f'Média de vacinados com {lista_vacinas[analise_vacinados]}: {media_por_vacina}')
            print(separador)
        print(separador)
        print(f'{separador}\n'
              f'1 - {lista_comandos_iniciais[0]}\n'
              f'2 - {lista_comandos_iniciais[1]}\n'
              f'3 - {lista_comandos_iniciais[2]}\n'
              f'0 - Encerra o Programa.\n'
              f'{separador}')
        comando_inicial = int(input('Digite o comando que deseja execultar: '))

    elif comando_inicial == 3:
        validacao = sum(estoque_geral[0]) + sum(estoque_geral[1]) + sum(estoque_geral[2])
        escolha_usuario_estoque = ''
        if validacao <= 0:
            print('Estoque vazio, primeiro adicione estoque.\n\n')
            escolha_usuario_estoque = input('Deseja cadastrar estoque? [S/N]: ').upper()
            if escolha_usuario_estoque[0] == 'S':
                comando_inicial = 2
            else:
                print(f'{separador}\n'
                      f'1 - {lista_comandos_iniciais[0]}\n'
                      f'2 - {lista_comandos_iniciais[1]}\n'
                      f'3 - {lista_comandos_iniciais[2]}\n'
                      f'0 - Encerra o Programa.\n'
                      f'{separador}')
                comando_inicial = int(input('Digite o comando que deseja execultar: '))
        elif validacao != 0 and validacao > 0:
            print(separador)
            print(f'{"*" * 10:^5} ESTOQUE DE VACINAS {"*" * 10:^5}')
            print(f'Total de vacinas em Estoque: {validacao}\n'
                  f'Média diária(Total vacinas): {validacao/30:.0f}\n'
                  f'Média diária {lista_vacinas[1]}: {sum(estoque_geral[0])/30:.0f}\n'
                  f'Média diária {lista_vacinas[2]}: {sum(estoque_geral[1])/30:.0f}\n'
                  f'Média diária {lista_vacinas[3]}: {sum(estoque_geral[2])/30:.0f}')
            break

    elif comando_inicial == 0:
        break
