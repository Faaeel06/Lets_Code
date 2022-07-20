<<<<<<< HEAD
<<<<<<< HEAD
import pandas as pd
import numpy as np
import random as rnd


base_dados = pd.read_csv("titanic.csv")
count_sex = base_dados['Sex'].value_counts()
media_age = base_dados['Age'].mean()
survive = (base_dados['Survived'] == 1).sum()
passanger_filter = base_dados.loc[base_dados['Name'] == "Montvila, Rev. Juozas"]
children = base_dados['Age'] < 18
male_adult = (base_dados['Sex'] == 'male') & (base_dados['Age'] >= 18)
female_adult = (base_dados['Sex'] == 'female') & (base_dados['Age'] >= 18)


print('=' * 20, '\n', count_sex, '\n', '=' * 20)
print('=' * 20, '\n', media_age, '\n', '=' * 20)
print('=' * 20, '\n', survive, '\n', '=' * 20)
print('=' * 20, '\n', passanger_filter, '\n', '=' * 20)
print('=' * 20, '\n', {'Criança': (base_dados[children]['Survived'].sum()),
                       'Homens': (base_dados[male_adult]['Survived'].sum()),
                       'Mulheres': (base_dados[female_adult]['Survived'].sum())}, '\n', '=' * 20)

>>>>>>> 3f17da5 (Projeto Aula)
=======
import pandas as pd
import numpy as np
import random as rnd


base_dados = pd.read_csv("titanic.csv")
count_sex = base_dados['Sex'].value_counts()
media_age = base_dados['Age'].mean()
survive = (base_dados['Survived'] == 1).sum()
passanger_filter = base_dados.loc[base_dados['Name'] == "Montvila, Rev. Juozas"]
children = base_dados['Age'] < 18
male_adult = (base_dados['Sex'] == 'male') & (base_dados['Age'] >= 18)
female_adult = (base_dados['Sex'] == 'female') & (base_dados['Age'] >= 18)


print('=' * 20, '\n', count_sex, '\n', '=' * 20)
print('=' * 20, '\n', media_age, '\n', '=' * 20)
print('=' * 20, '\n', survive, '\n', '=' * 20)
print('=' * 20, '\n', passanger_filter, '\n', '=' * 20)
print('=' * 20, '\n', {'Criança': (base_dados[children]['Survived'].sum()),
                       'Homens': (base_dados[male_adult]['Survived'].sum()),
                       'Mulheres': (base_dados[female_adult]['Survived'].sum())}, '\n', '=' * 20)
>>>>>>> a766d2b (Atualização de aulas)
