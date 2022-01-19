#Empty cells
# Data in wrong format
# Wrong data
# Duplicates

import pandas as pd

df = pd.read_csv('pandas/usuariosWrongData.csv')
print(df.to_string()) #aca aparecen NaN values
new_df = df.dropna() #elimina las rows/filas que les faltan valores pero no las vacias, can return a nuew data frame
print(new_df.to_string())

#df.dropna(inplace = True) not return a new data frame, but modify the original data frame
#Print(df.to_string()) #remove rows with null values, for example 8 index

#replace NA values, NO LOS ELIMINA como dropna
df.fillna('REEMPLAZADO', inplace=True)
print(df.to_string())

#Replace for especified columns, no funciona
# df[0].fillna('AA', inplace=True)
# print(df.to_string())

