import requests
from bs4 import BeautifulSoup
import collections

url = 'https://logosklogos.com/interlinear/AT/Gn'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

palabras = soup.findAll('span', class_="text-danger translation-hebrew")
tipos_palabra = soup.findAll(
    'span', class_="gw parsing cursor-pointer text-warning")
palabras_hebreo = soup.findAll(
    'span', class_="gw cursor-pointer hebrew-ezra-bold interl text-success")

codigos_diccionario = soup.select('td a')

for palabra, tipo_palabra, palabra_hebreo, codigo_diccionario in zip(palabras, tipos_palabra, palabras_hebreo, codigos_diccionario):
    dic = {}
    dic['palabra'] = palabra.string
    dic['tipo_palabra'] = tipo_palabra['title']
    dic['palabra_hebreo'] = palabra_hebreo['title']
    dic['codigo_diccionario'] = codigo_diccionario['href']
    print(dic)
