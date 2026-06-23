import re

def cpf_is_valid(cpf):
    cpf = re.sub(r"\D", "", str(cpf))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    return True


def validate_cpf_column(df, config):
    column = config["column"]
    df["cpf_status"] = df[column].apply(
        lambda x:
        "VALIDO"
        if cpf_is_valid(x)
        else "INVALIDO")

    return df