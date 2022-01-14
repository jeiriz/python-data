#Library, used to analyze data and make conclusions based on statistical theories
# has functions for analyzing, cleaning, exploring and manipulating data, for example, we can know the max value, the average, correlation between two variables
import pandas as pd

myData = {
    "Autos": ["Volvo", "Ford"],
    "Año": [1995,2001]
}

# 2 dimensional data [columns and rows], but can be multidimensional
df = pd.DataFrame(myData)

#Me imprimira una tabla con las columnas que agregué y un indice
print(df)

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


