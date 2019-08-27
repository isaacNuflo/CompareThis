import argparse
import re
from requests_utils import do_request, get_response_text, get_libros
from scraper import do_scraper

API_KEY = 'eb263e4daba65f0d144c7f01ca6b9522'
REGEX_LIBRO = r'[1-2]?[\s]?[a-zA-Z]+'
REGEX_CITA = r'[1-9]\d{0,2}\:[1-9]\d{0,2}'
API_URL = 'https://api.biblia.com/v1/bible/content/RVR60.txt.json?passage={}&key={}'


def compare(versiculo):
    if versiculo:
        libro = re_search(REGEX_LIBRO, versiculo)
        cita = re_search(REGEX_CITA, versiculo)
        if libro and cita:
            request = build_api_request(libro,cita)
            response = do_request(request)
            texto = get_response_text(response)
            print(texto)
        else:
            print('Versiculo mal escrito')
    else:
        print('Ingrese un versiculo a consultar')


def init():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--versiculo", help="Versiculo a consultar")
    return parser.parse_args()


def build_api_request(libro, cita):
    libros = get_libros()
    testamento_abrv = 'AT'
    testamento = libros.get(testamento_abrv, '')
    libro_ingles = testamento.get(libro, "")
    if libro_ingles is '':
        testamento_abrv = 'NT'
        testamento = libros.get(testamento_abrv, '')
        libro_ingles = testamento.get(libro, '')
    libro_abrv = libro_ingles.get('abreviacion','')
    cita = cita.replace(":", ".")
    numeros = cita.split('.')
    print(do_scraper(testamento_abrv, libro_abrv, numeros[0], numeros[1]))
    return API_URL.format(libro_ingles.get("nombre", "") + cita, API_KEY)


def re_search(regex, cadena):
    return re.search(regex, cadena).group(0)
