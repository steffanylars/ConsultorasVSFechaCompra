import pandas as pd

# 1. Importar el archivo CSV
df = pd.read_csv('DB/analysis_MonthlyOrdersByDay_PV.csv')

# 2. Contar duplicados en una columna específica (ejemplo: 'id_usuario')
# value_counts() cuenta ocurrencias y los ordena
conteo_duplicados = df['OrderKEY'].value_counts()

# 3. Filtrar para ver solo los que están repetidos (más de 1 vez)
duplicados = conteo_duplicados[conteo_duplicados > 1]

print("Claves repetidas y su número de ocurrencias:")
print(len(duplicados))
