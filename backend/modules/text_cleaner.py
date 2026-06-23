import re

def clean_text(text):

    if text is None:
        return text

    text = str(text)
    text = re.sub(r"[^A-Za-zÀ-ÿ0-9 ]","", text)
    text = text.strip()

    return text


def clean_text_column(df, config):
    column = config["column"]
    df[column] = df[column].apply(clean_text)
    
    return df