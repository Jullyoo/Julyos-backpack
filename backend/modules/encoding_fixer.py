def fix_encoding(text):

    if text is None:
        return text

    try:
        return (str(text).encode("latin1").decode("utf-8"))

    except:
        return text


def fix_encoding_column(df, config):
    column = config["column"]
    df[column] = df[column].apply(fix_encoding)
    return df