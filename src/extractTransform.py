import requests
import pandas as pd

def extrair_dados_dolar(inicio: str, fim: str) -> pd.DataFrame:
    url = (
        f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
        f"CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
        f"?@dataInicial='{inicio}'&@dataFinalCotacao='{fim}'&$top=10000&$format=json"
    )
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()["value"]
    return pd.DataFrame(dados)

def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    df['dataHoraCotacao'] = pd.to_datetime(df['dataHoraCotacao'])
    df = df.rename(columns={
        'cotacaoCompra': 'compra',
        'cotacaoVenda': 'venda',
        'dataHoraCotacao': 'data'
    })
    df['media'] = df[['compra', 'venda']].mean(axis=1)
    df = df[['data', 'compra', 'venda', 'media']].dropna().sort_values('data')
    return df
