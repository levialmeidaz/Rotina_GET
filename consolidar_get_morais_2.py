import os
import pandas as pd

# Caminho da pasta de origem e destino
pasta_ajustado = r'C:\Users\indic\OneDrive - grupojb.log.br\Morais\SLA\Respostas_GET_Ajustado'
pasta_consolidado = r'C:\Users\indic\OneDrive - grupojb.log.br\Morais\SLA\Respostas_GET_Consolidado'

# Cria a pasta de destino, se não existir
os.makedirs(pasta_consolidado, exist_ok=True)

# Lista para armazenar os DataFrames
dfs = []

# Passo 1: Percorre todos os arquivos .csv da pasta ajustada
for arquivo in os.listdir(pasta_ajustado):
    if arquivo.endswith('.csv'):
        caminho_csv = os.path.join(pasta_ajustado, arquivo)
        
        # Lê o arquivo CSV
        df = pd.read_csv(caminho_csv, encoding='utf-8')
        
        # Adiciona o DataFrame à lista
        dfs.append(df)

# Passo 2: Combina todos os DataFrames em um único DataFrame
df_consolidado = pd.concat(dfs, ignore_index=True)

# Passo 3: Define o caminho para salvar o arquivo consolidado
caminho_consolidado = os.path.join(pasta_consolidado, 'Consolidado_GET.csv')

# Passo 4: Salva o DataFrame consolidado como CSV UTF-8
df_consolidado.to_csv(caminho_consolidado, index=False, encoding='utf-8-sig')

print(f'Arquivo consolidado salvo em {caminho_consolidado}')