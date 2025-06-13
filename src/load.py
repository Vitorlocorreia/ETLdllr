import pandas as pd

def salvar_csv(df: pd.DataFrame, caminho: str, sep: str = ";", decimal: str = ","):
    df.to_csv(caminho, sep=sep, decimal=decimal, index=False)