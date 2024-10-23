import pandas as pd
import openpyxl

excel = pd.read_excel(r"C:\Users\anaju\OneDrive\Documentos\netflix_titles.xlsx", header = 1)
df = pd.DataFrame(excel)

#Exibindo o DataFrame
print(df)

#Quais colunas estão presentes no dataset?
print(f"As colunas do dataset são: {df.columns}")

#Quantos filmes estão disponíveis na Netflix?
#shape[0] refere-se ao número de linhas de um dataframe, e 1 às colunas
filmes = df[df["type"] == "Movie"].shape[0]
disp = df[df["type"] == 'Movie']
print(f"A quantidade de filmes disponíveis no catálogo são: {filmes}")
print(f"A lista de filmes disponíveis no catálogo são: {disp}")

#Quem são os 5 diretores com mais filmes e séries na plataforma?
topDiretores = df["director"].value_counts().head(5)
print(f"Os 5 diretores com mais filmes e séries na plataforma são: {topDiretores}")

#Quais diretores também atuaram como atores em suas próprias produções?
same = df[df["director"] == df["cast"]]
quantidade = same.shape[0]
print(f"Quantidade de diretores que também atuaram como atores: {quantidade}")
print(f"A lista de diretores que também atuaram em suas produções são: {same}")

#Insight interessante: a quantidade de filmes lançados no ano mais recente (2021) foram de: 592
#Converte a coluna 'release_year' para numérico
df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")
#Verifica os valores únicos na coluna 'release_year'
#print(df["release_year"].unique())
filmes_2021 = df[df["release_year"] == 2021]
quantidade_filmes_2021 = filmes_2021.shape[0]
print(f"Quantidade de filmes lançados em 2021: {quantidade_filmes_2021}")
print(f"Filmes lançados em 2021: {filmes_2021["title"].tolist()}")





