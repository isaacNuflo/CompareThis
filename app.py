import requests
import argparse
import json
import re

API_KEY = 'eb263e4daba65f0d144c7f01ca6b9522'
REGEX_LIBRO = r'[1-2]?[\s]?[a-zA-Z]+'
REGEX_CITA = r'[1-9]\d{0,2}\:[1-9]\d{0,2}'
URL_API = 'https://api.biblia.com/v1/bible/content/RVR60.txt.json?passage={}&key={}'


def compare():
    if aversiculo:
        libro = re_search(REGEX_LIBRO, versiculo)
        cita = re_search(REGEX_CITA, versiculo)
        if libro and cita:
            texto = do_request(libro, cita)
            print(texto)
        else:
            print('Versiculo mal escrito')
    else:
        print('Ingrese un versiculo a consultar')


def get_libros():
    with open('libros.json') as json_file:
        return json.load(json_file)


def init():
    parser.add_argument(
        "-v", "--versiculo", help="Versiculo a consultar")
    return parser.parse_args()


def do_request(libro, cita):
    testamento = libros.get("AT", "")
    libro_ingles = testamento.get(libro, "")
    if libro_ingles is "":
        testamento = libros.get("NT", "")
        libro_ingles = testamento.get(libro, "")
    cita = cita.replace(":", ".")
    request = URL_API.format(libro_ingles.get("nombre", "") + cita, API_KEY)
    response = requests.get(request)

    return json.loads(response.content.decode('utf-8'))["text"]


def re_search(regex, cadena):
    return re.search(regex, cadena).group(0)


parser = argparse.ArgumentParser()
args = init()
libros = get_libros()
compare(args.versiculo)
