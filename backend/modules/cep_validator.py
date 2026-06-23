import re

def cep_is_valid(cep):
    cep = re.sub( r"\D", "", str(cep))
    return len(cep) == 8


def validate_cep_column(df, config):
    column = config["column"]
    df["cep_status"] = df[column].apply(
        lambda x:
        "VALIDO"
        if cep_is_valid(x)
        else "INVALIDO")
    return df