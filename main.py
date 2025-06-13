import pandas as pd
from src.etl_dolar.extract_dolar import extrair_dados_dolar
from src.etl_dolar.transform_dolar import transformar_dados
from src.etl_dolar.load_dolar import salvar_csv


dados_bcb = extrair_dados_dolar("01-01-2023", "01-06-2023")
dados_tratados = transformar_dados(dados_bcb)
salvar_csv(dados_tratados, "src/datasets/cotacoes_dolar.csv", ";", ",")
