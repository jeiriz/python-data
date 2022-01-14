import pandas as pd

df = pd.read_json("usrsDictLista.json") #este json es un diccionario con lista
print(df)

df = pd.read_json("usrsDictDict.json") #este json es un diccionario con diccionarios
print (df)