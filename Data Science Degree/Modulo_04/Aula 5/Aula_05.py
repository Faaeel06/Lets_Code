
import pandas as pd
import random
separeted = '=' * 30
gastos = {"Meus Gastos": [random.randint(1, 100) for i in range(1, 31)]}
df_meus_gastos = pd.DataFrame(gastos)

print(df_meus_gastos.head(), '\n', separeted)

print(df_meus_gastos['Meus Gastos'].cumsum(), '\n', separeted)

import pandas as pd
import random
separeted = '=' * 30
gastos = {"Meus Gastos": [random.randint(1, 100) for i in range(1, 31)]}
df_meus_gastos = pd.DataFrame(gastos)

print(df_meus_gastos.head(), '\n', separeted)

print(df_meus_gastos['Meus Gastos'].cumsum(), '\n', separeted)
