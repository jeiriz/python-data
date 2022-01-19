#Library, used to analyze data and make conclusions based on statistical theories
# has functions for analyzing, cleaning, exploring and manipulating data, for example, we can know the max value, the average, correlation between two variables
import pandas as pd

myData = {
    "Autos": ["Volvo", "Ford"],
    "Año": [1995,2001]
}

# 2 dimensional data [columns and rows], its a table
df = pd.DataFrame(myData)

#Me imprimira una tabla con las columnas que agregué y un indice
print(df)
print(df["Autos"])
print(df[0:2])
print("========")
# Localiza la fila 1, la cual contiene Ford y 2001, a su vez, imprime la columna 
print(df.loc[1]) # o loc[[0,1]] si no se pone doble lista, rompe, #first row of the dataframe

#Ademas de localizar rows, podes localizar index
df = pd.DataFrame(myData, index = ["A","B"]) #eso sirve cuando queres cargar una variable tipo lista o diccionario, no es csv o json
print(df.loc["A"])

#Series == column in table, unidimensional
columnaSerieList = pd.Series([1,2,3])
print(columnaSerieList)

#Series with object, la clave seria el index, es decir, los labels
columnaSerieObject = pd.Series({
    "Dia1": "Lunes",
    "Dia2": "Martes",
})
print(columnaSerieObject)

#Labels == index automatico que se coloca, unidimensional
#Se pueden modificar

columnaSerie = pd.Series(["Auto", "Moto"], index=["x","y"])
print(columnaSerie)
print(columnaSerie["y"])



