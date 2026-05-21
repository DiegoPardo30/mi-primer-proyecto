import pandas as pd

# Leer el CSV con encoding correcto
df = pd.read_csv("ventas_meli.csv", encoding="latin-1")

print("=== Columnas disponibles ===")
for i, col in enumerate(df.columns):
    print(f"{i}: '{col}'")

print(f"\n=== Total de columnas: {len(df.columns)} ===")