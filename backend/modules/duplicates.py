def remove_duplicates(df, config):

    subset = config.get("columns")
    before = len(df)
    df = df.drop_duplicates(subset=subset)
    after = len(df)
    print(f"{before-after} duplicados removidos")
    return df