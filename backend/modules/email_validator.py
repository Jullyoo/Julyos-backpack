import re

EMAIL_REGEX = re.compile( r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" )

def validate_email(email):

    if not email:
        return False

    return bool(EMAIL_REGEX.match(str(email)))


def validate_email_column(df, config):
    column = config.get("column", "email")

    df["email_status"] = df[column].apply(
        lambda x:
        "VALIDO"
        if validate_email(x)
        else "INVALIDO")

    return df

