import requests
import argparse
import json
import re

API_KEY = 'MY_API_KEY'
with open('libros.json') as json_file:
    libros = json.load(json_file)

parser = argparse.ArgumentParser()
parser.add_argument(
    "-v", "--versiculo", help="Versiculo a consultar")
args = parser.parse_args()

if args.versiculo:
    libro = re.search(r'[1-2]?[\s]?[a-zA-Z]+', args.versiculo).group(0)
    cita = re.search(r'[1-9]\d{0,2}\:[1-9]\d{0,2}', args.versiculo).group(0)
    if libro and cita:
        libro_ingles = libros[libro]
        cita = cita.replace(":", ".")

        request = 'https://api.biblia.com/v1/bible/content/RVR60.txt.json?passage={}&key={}'.format(
            libro_ingles + cita, API_KEY)

        response = requests.get(request)

        texto = json.loads(response.content.decode('utf-8'))["text"]

        print(texto)
    else:
        print('Versiculo mal escrito')
else:
    print('Ingrese un versiculo a consultar')
