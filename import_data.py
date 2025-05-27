import pandas as pd

# 1 - Importando dados iniciais
data = pd.read_excel("data/VendaCarros.xlsx")

print (data)

# 2 - Lista os primeiros registros
print(data.head(15))

# 3 - Lista os últimos registros
print(data.tail(10))

# 4 - Contagem de valores por Fabricante
print(data['Fabricante'].value_counts())