import pandas as pd

#head

df = pd.read_csv('pandas/usuarios.csv')
print(df.head(2)) #imprime los primeros 2 registros, ademas de los encabezados, si no se especifica se imprimen 5

#tail
print(df.tail(2)) #print the last x rows

#info, describe dtypes, memory, range index, total columns, if there is a null value
print(df.info())

