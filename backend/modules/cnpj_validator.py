import re

def cnpj_is_valid(cnpj):
    cnpj = re.sub(r"\D", "", str(cnpj))
    if len(cnpj) != 14:
        return False
    if cnpj == cnpj[0] * 14:
        return False
    return True


def validate_cnpj_column(df, config):
    column = config["column"]
    df["cnpj_status"] = df[column].apply(
        lambda x:
        "VALIDO"
        if cnpj_is_valid(x)
        else "INVALIDO")

    return df