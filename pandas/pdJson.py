import pandas as pd

df = pd.read_json("pandas/usrsDictLista.json") #este json es un diccionario con lista
print(df)

df2 = pd.read_json("pandas/usrsDictDict.json") #este json es un diccionario con diccionarios
print (df2)