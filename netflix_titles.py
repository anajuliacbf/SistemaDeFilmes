import pandas as pd
import openpyxl

excel = pd.read_excel(r"C:\Users\anaju\OneDrive\Documentos\desafioVEXpenses\netflix_titles.xlsx", header = 1)
df = pd.DataFrame(excel)

#Exibindo o DataFrame
print(df)

#Quais colunas estão presentes no dataset?
#Exibe as colunas do df
print(f"As colunas do dataset são: {df.columns}")

#Quantos filmes estão disponíveis na Netflix?
#Filtra a coluna "type" por "Movie", shape[0] refere-se ao número de linhas de um dataframe
filmes = df[df["type"] == "Movie"].shape[0]
disp = df[df["type"] == 'Movie']
print(f"A quantidade de filmes disponíveis no catálogo são: {filmes}")
print(f"A lista de filmes disponíveis no catálogo são: {disp}")

#Quem são os 5 diretores com mais filmes e séries na plataforma?
#Conta a quantidade de diretores que aparecem na coluna, e em seguida exibe os top 5
topDiretores = df["director"].value_counts().head(5)
print(f"Os 5 diretores com mais filmes e séries na plataforma são: {topDiretores}")

#Quais diretores também atuaram como atores em suas próprias produções?
#Verifica quais linhas possuem o mesmo valor nas colunas 'director' e 'cast'
same = df[df["director"] == df["cast"]]
#Contar quantos diretores também atuaram como atores
quantidade = same.shape[0]
print(f"Quantidade de diretores que também atuaram como atores: {quantidade}")
print(f"A lista de diretores que também atuaram em suas produções são: {same}")

#Explore o dataset e compartilhe um insight ou número que você considere interessante.
#Insight interessante: a quantidade de filmes lançados no ano mais recente (2021) foram de: 592
# Converte a coluna 'release_year' para numérico
df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")
# Verifica os valores únicos na coluna 'release_year'
#print(df["release_year"].unique())
#Filtra os filmes que foram lançados em 2021
filmes_2021 = df[df["release_year"] == 2021]
#Exibe a quantidade de filmes lançados em 2021
quantidade_filmes_2021 = filmes_2021.shape[0]
print(f"Quantidade de filmes lançados em 2021: {quantidade_filmes_2021}")
# Exibe os títulos dos filmes lançados em 2021
print(f"Filmes lançados em 2021: {filmes_2021["title"].tolist()}")





