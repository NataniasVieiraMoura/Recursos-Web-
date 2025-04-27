import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Criando os DataFrames de exemplo

df1 = pd.DataFrame({
    'Ano': np.arange(2010, 2021),
    'Vendas': np.random.randint(100, 500, 11)
})

df2 = pd.DataFrame({
    'Produto': ['Mouses', 'Teclados', 'Headsets', 'Monitores', 'Mousepads'],
    'Lucro': np.random.uniform(500, 2000, 5)
})

df3 = pd.DataFrame({
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Custos': np.random.randint(1000, 5000, 12)
})

# Filtrando dados
filtro_df1 = df1[df1['Vendas'] > 300]
filtro_df2 = df2[df2['Lucro'] > 1000]
filtro_df3 = df3[df3['Custos'] < 4000]

# Criando gráficos
plt.figure(figsize=(15, 5))

# Gráfico de linha para Vendas ao longo do ano
plt.subplot(1, 2, 1)
sns.lineplot(data=df1, x='Ano', y='Vendas', marker='o', color='b')
plt.title('Vendas ao longo dos anos')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.grid(True)

# Gráfico de barras para Lucro por produtos
plt.subplot(1, 2, 2)
sns.barplot(data=df2, x='Produto', y='Lucro', palette='viridis')
plt.title('Lucro por Produto')
plt.xlabel('Produto')
plt.ylabel('Lucro')

plt.tight_layout()
plt.show()

# Segundo gráfico de barras para Custos mensais
plt.figure(figsize=(10, 5))
sns.barplot(data=df3, x='Mês', y='Custos', palette='coolwarm')
plt.title('Custos Mensais')
plt.xlabel('Mês')
plt.ylabel('Custos')
plt.xticks(rotation=45)
plt.show()