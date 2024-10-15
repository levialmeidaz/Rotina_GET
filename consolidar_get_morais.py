import os
import pandas as pd

# Caminho da pasta de origem e de destino
pasta_origem = r'C:\Users\indic\OneDrive - grupojb.log.br\Morais\SLA\Resposta GET - Filiais'
pasta_destino = r'C:\Users\indic\OneDrive - grupojb.log.br\Morais\SLA\Respostas_GET_Ajustado'

# Cria a pasta de destino, se não existir
os.makedirs(pasta_destino, exist_ok=True)

# Lista de colunas a serem mantidas e a ordem correta
colunas_padrao = ['Data do Arquivo', 'TIPO DE VENDA', 'TRP', 'FILIAL', 'Pedido', 'Nota', 'DOC_VENDA', 'SITUAÇÃO_CN',
                  'cod.consultora', 'Ação', 'NAT - Dynamics', 'Etapa', 'Range', 'CD', 'CHAVE', 'Flag_Max', 'CONTAGEM',
                  'Contagem Nats', 'Tem Nat?', 'CHAVE COMPLETA', 'Qtd. Saídas para entrega', 'Cidade',
                  'Último motivo de retorno', 'REGIÃO', 'Dias Entre', 'Range2', 'Range3', 'Última Ocorrência',
                  'Data Última Ocorrência', 'Vencimento', 'Data de Criação da NAT', 'NAT', 'Etapa NAT',
                  'Solução NATs', 'Resposta TRP', 'NAT foi respondida?', 'Filial2', 'Término Real (Base NAT)',
                  'Devido ou indevido', 'QTD Share Point', 'Repetidos de Ontem', 'Taxa de Repetição', 
                  'Endereço modificado?', 'Retorno SharePoint', 'Análise Sharepoint', 'Primeira DT no GET',
                  'Dias no GET', 'RANGE GET', 'Lançamento NATs']

# Percorre todos os arquivos da pasta de origem
for arquivo in os.listdir(pasta_origem):
    if arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)
        
        # Lê apenas a primeira aba do arquivo Excel
        df = pd.read_excel(caminho_arquivo, sheet_name=0)
        
        # Verifica se a coluna 'Data do Arquivo' já existe no arquivo
        if 'Data do Arquivo' in df.columns:
            print(f"'Data do Arquivo' já presente no arquivo {arquivo}. Mantendo a informação existente.")
        
        # Mantém as colunas padrão, preenchendo com NaN as que não existirem
        df = df.reindex(columns=colunas_padrao)
        
        # Define o caminho de destino para salvar o arquivo como CSV
        nome_arquivo_csv = f"{os.path.splitext(arquivo)[0]}.csv"
        caminho_arquivo_destino = os.path.join(pasta_destino, nome_arquivo_csv)
        
        # Salva o DataFrame ajustado como .csv
        df.to_csv(caminho_arquivo_destino, index=False, encoding='utf-8-sig')
        
        print(f'Arquivo {arquivo} processado e salvo como {nome_arquivo_csv} em {pasta_destino}')

print('Processo concluído!')