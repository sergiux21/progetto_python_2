import pandas as pd

#funzione per caricare un csv
def load_csv(path):
    return pd.read_csv(path)

#funzione per caricare un excel
def load_excel(path):
    return pd.read_excel(path)