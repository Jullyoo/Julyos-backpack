def remove_nulls(df, config):
    
    how = config.get("how", "any")
    before = len(df)
    df = df.dropna(how=how)
    after = len(df)
    print(f"{before-after} linhas removidas")
    return df