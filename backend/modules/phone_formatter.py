import re

def normalize_phone(phone):

    if phone is None:
        return None

    phone = re.sub(r"\D", "", str(phone))

    if len(phone) == 11:
         phone = "55" + phone
    return phone


def format_phone_column(df, config):
    column = config["column"]
    df[column] = df[column].apply(normalize_phone)
    return df