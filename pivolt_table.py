import pandas as pd

# 1 - Importando os dados
data = pd.read_excel("data/VendaCarros.xlsx")
#print(type (data))

# 2 - Selecionando colunas específicas do dataframe
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

# 3 - Criando a tabela pivô
pivolt_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivolt_table)

# 4 - Exportando a tabela pivô em arquivo excel
pivolt_table.to_excel("data/pivolt_table.xlsx", "Relatorio")