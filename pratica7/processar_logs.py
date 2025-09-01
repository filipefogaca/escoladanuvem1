import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    media_tempo = df['']