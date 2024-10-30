import pandas as pd
import numpy as np

file_path_vendas = './vendas-por-fatura.csv'
data_vendas = pd.read_csv(file_path_vendas)

data_vendas['Valor'] = data_vendas['Valor'].str.replace(',', '.').astype(float)
data_vendas['Valor'] = data_vendas['Valor'].abs()

data_vendas['Data da fatura'] = pd.to_datetime(data_vendas['Data da fatura'], errors='coerce')

median_quantity = data_vendas['Quantidade'][data_vendas['Quantidade'] > 0].median()
data_vendas['Quantidade'] = np.where(data_vendas['Quantidade'] < 0, median_quantity, data_vendas['Quantidade'])

data_vendas['País'] = data_vendas['País'].replace({'UK': 'United Kingdom', 'USA': 'United States'})

data_vendas['Mes'] = data_vendas['Data da fatura'].dt.month
data_vendas['Ano'] = data_vendas['Data da fatura'].dt.year

data_vendas['Cadastro_Completo'] = np.where(data_vendas['ID Cliente'].notna(), 'Completo', 'Incompleto')

data_vendas.columns = ['NFat', 'Data', 'CliID', 'Pais', 'QTD', 'Valor', 'Mes', 'Ano', 'Status']

cleaned_file_path_vendas = './vendas_por_fatura_cleaned.csv'
data_vendas.to_csv(cleaned_file_path_vendas, index=False)
cleaned_file_path_vendas