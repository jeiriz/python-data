import pandas as pd

df = pd.read_csv("pandas/usuarios.csv")
print(df)
print(df.to_string()) #imprime todo el dataframe 
pd.options.display.max_rows = 2
print(pd.options.display.max_rows) #limite de cuantas filas imprime, se puede modificar



