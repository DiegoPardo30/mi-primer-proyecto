import pandas as pd

# Leer el CSV con encoding correcto
df = pd.read_csv("ventas_meli.csv", encoding="latin-1")

print("=== Primeras 5 filas ===")
print(df.head())

print("\n=== Información general ===")
print(f"Total de ventas: {len(df)}")
print(f"Total de unidades vendidas: {df['Unidades'].sum()}")
print(f"Ingresos totales: ${df['Total (MXN)'].sum():,.2f} MXN")

print("\n=== Top 10 SKUs por unidades vendidas ===")
top_skus = df.groupby("SKU").agg({
    "Unidades": "sum",
    "Ingresos por productos (MXN)": "sum",
    "Total (MXN)": "sum"
}).sort_values("Unidades", ascending=False).head(10)
print(top_skus)

print("\n=== Resumen por estado de venta ===")
por_estado = df.groupby("Estado").agg({
    "Unidades": "sum",
    "Total (MXN)": "sum"
}).round(2)
print(por_estado)