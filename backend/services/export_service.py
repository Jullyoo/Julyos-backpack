import os

def export_csv(df, filename):
    os.makedirs("outputs", exist_ok=True)
    output_path = os.path.join("outputs", filename)
    df.to_csv(output_path, index=False)
    return output_path