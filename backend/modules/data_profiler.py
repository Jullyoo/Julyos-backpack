import pandas as pd

def generate_profile(df):

    profile = {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicates": int(df.duplicated().sum()),
        "nulls": int(df.isna().sum().sum()),
        "memory_mb":round(df.memory_usage(deep=True).sum()/ 1024 / 1024, 2)
    }

    profile["quality_score"] = calculate_score(profile)
    return profile

def calculate_score(profile):
    score = 100
    score -= (profile["duplicates"] * 0.1)
    score -= (profile["nulls"] * 0.05)

    return max(0, round(score))