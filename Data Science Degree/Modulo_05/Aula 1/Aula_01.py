import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import sleep


def graph():
    path_file = input('Digite o caminho do arquivo: ')
    df = pd.read_csv(f'{path_file}')
    print(df)

    df_vendas = pd.DataFrame(
        {'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Jan', 'Fev', 'Mar', 'Abr', 'Jan', 'Fev', 'Mar', 'Abr'],
         'Vendas': np.random.randint(low=100, size=12),
         'Produto': np.repeat(['Samsung', 'Apple', 'Motorola'], 4)})

    def data_presentation():
        df.info()

    data_presentation()

    def graph_mount():
        graph_data = df.copy()
        menu = (f'0 - Encerrar análise\n',
                f'1 - Pontos\n',
                f'2 - Linhas\n',
                f'3 - Pizza\n',)
        print(menu)
        sleep(0.5)
        tipo = int(input('Digite o tipo que deseja ver? '))
        if tipo == 0:
            pass
        elif tipo == 1:
            ax = ''
            ax_2 = ''
            menu_opcao = (f'0 - Encerrar\t'
                          f'1 - Geral\t',
                          f'2 - Mulheres\t',
                          f'3 - Homens\t')
            print(menu_opcao)
            opcao = int(input('Qual opção deseja ver? '))
            if opcao == 0:  # Encerra o sub_menu
                pass
            elif opcao == 1:  # Gráfico Geral por idade
                ax = graph_data[df['Sex'] == 'female'].plot(x='Age', y='Fare', kind='scatter', figsize=(10, 5),
                                                            title='Meu Primeiro Gráfico', fontsize=15, color='red',
                                                            s='Age')
                graph_data[df['Sex'] == 'male'].plot(x='Age', y='Fare', kind='scatter', figsize=(10, 5),
                                                     title='Meu Primeiro Gráfico',
                                                     fontsize=15, color='blue', ax=ax)
                plt.show()
                opcao = int(input('Qual opção deseja ver? '))
                return opcao
            elif opcao == 2:  # Gráfico dados Mulheres
                graph_data[df['Sex'] == 'female'].plot(x='Age', y='Fare', kind='scatter', figsize=(10, 5),
                                                       title='Mulheres', fontsize=15, color='red',
                                                       s='Age')
                plt.show()
                opcao = int(input('Qual opção deseja ver? '))
                return opcao
            elif opcao == 3:  # Gráfico dados Homens
                graph_data[df['Sex'] == 'male'].plot(x='Age', y='Fare', kind='scatter', figsize=(10, 5),
                                                     title='Homens',
                                                     fontsize=15, color='blue')
                plt.show()
                opcao = int(input('Qual opção deseja ver? '))
                return opcao
            else:
                print('Opção inválida.\nDigite a opção correta ou encerre o programa.')
                sleep(0.5)
                print(menu_opcao)
                sleep(0.5)
                opcao = int(input('Qual opção deseja ver? '))
                return opcao
            sleep(0.5)
            print(menu)
            sleep(0.5)
            tipo = input('Digite o tipo que deseja ver? ')
        elif tipo == 2:
            # MANUAL
            ax1 = df_vendas[df_vendas['Produto'] == 'Samsung'].plot(x='Mês',
                                                                    y='Vendas',
                                                                    kind='line',
                                                                    label='Samsung',
                                                                    color='blue')
            ax2 = df_vendas[df_vendas['Produto'] == 'Apple'].plot(x='Mês',
                                                                  y='Vendas',
                                                                  kind='line',
                                                                  label='Apple',
                                                                  color='green',
                                                                  ax=ax1)
            ax3 = df_vendas[df_vendas['Produto'] == 'Motorola'].plot(x='Mês',
                                                                     y='Vendas',
                                                                     kind='line',
                                                                     label='Samsung',
                                                                     color='red',
                                                                     ax=ax1)
            ax1.set_ylabel('Vendas')
            ax1.legend(title='Produto')

            # PIVOTADO
            df_vendas.pivot(index='Mês', columns='Produto', values='Vendas').plot(kind='line')
            df_vendas['Mês'] = pd.Categorical(df_vendas['Mês'],
                                              categories=['Jan', 'Fev', 'Mar', 'Abr'],
                                              ordered=True)
            df_vendas.pivot(index='Mês', columns='Produto', values='Vendas').plot(kind='line',
                                                                                  figsize=(20, 10))
            plt.show()
            sleep(0.5)
            print(menu)
            sleep(0.5)
            tipo = int(input('Digite o tipo que deseja ver? '))
        elif tipo == 3:
            df_vendas.groupby(['Produto']).sum().plot(y='Vendas',
                                                      kind='pie',
                                                      autopct='%1.0f%%',
                                                      labeldistance=None)
            df_vendas.pivot(index='Mês',
                            columns='Produto',
                            values='Vendas').plot(subplots=True,
                                                  kind='pie',
                                                  figsize=(20, 10),
                                                  labeldistance=None,
                                                  autopct='%1.0f%%')
            df_vendas.pivot(index='Produto',
                            columns='Mês',
                            values='Vendas').plot(subplots=True,
                                                  kind='pie',
                                                  figsize=(20, 10),
                                                  labeldistance=None,
                                                  autopct='%1.0f%%')
            plt.show()
            sleep(0.5)
            print(menu)
            sleep(0.5)
            tipo = int(input('Digite o tipo que deseja ver? '))
        elif tipo == 4:
            pass
            sleep(0.5)
            print(menu)
            sleep(0.5)
            tipo = int(input('Digite o tipo que deseja ver? '))
        elif tipo == 5:
            pass
            sleep(0.5)
            print(menu)
            sleep(0.5)
            tipo = int(input('Digite o tipo que deseja ver? '))
        else:
            print('Opção inválida.\nDigite a opção correta ou encerre o programa.')
            sleep(0.5)
            print(menu)
            sleep(0.5)
            tipo = int(input('Digite o tipo que deseja ver? '))

    graph_mount()


graph()
