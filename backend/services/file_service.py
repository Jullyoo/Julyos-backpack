import pandas as pd

def read_file(file):
    filename = file.filename
    if filename.endswith(".csv"):
        return pd.read_csv(file)
    elif filename.endswith(".xlsx"):
        return pd.read_excel(file)
    raise Exception("Formato não suportado")