# Beautifull soup y requests
import requests as rq
from bs4 import BeautifulSoup as bs
import csv

url = 'https://coinmarketcap.com/all/views/all/'
response = rq.get(url)

# Analizar sintacticamente el contenido de la pagina
soup = bs(response.text, 'html.parser') #el text es el contenido en Unicode (standar de codificacion de caracteres dise;ado para ser legible)

criptos_name = soup.find_all('a', class_='cmc-table__column-name--name cmc-link')
criptos_price = soup.find_all('td', class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price')

criptos_name_list = []
for name in criptos_name:
    criptos_name_list.append(name.text)

criptos_price_list = []

for price in criptos_price:
    criptos_price_list.append(price.text)

# zip -> utiliza 2 listas/tuplas para crear otra lista con pares de elementos, es decir, elprimer elemento de la primera lista siendo su par el primer elemento de la segunda lista
for nombre,price in zip(criptos_name_list[0:2],criptos_price_list[0:2]):
    print(nombre,price)