import pandas as pd

def normalize_text(col):
    return (
        col.str.lower()
           .str.strip()
           .str.replace(r"\s+", "_", regex=True)
           .str.replace(r"[^a-z_]", "", regex=True)
    )

# df["job_title"] = normalize_text(df["job_title"]) Ejemplo de uso
