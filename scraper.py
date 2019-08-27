import requests
from requests_utils import do_request, get_beautifulsoup, do_findall, do_select, CLASS

LOGOS_URL = 'https://logosklogos.com/'
INTERLINEAL_URL = 'interlinear/{}/{}/{}/{}'


def build_interlineal_request(testamento, libro_Abrv, num_libro, num_versiculo):
    return LOGOS_URL + INTERLINEAL_URL.format(testamento, libro_Abrv, num_libro, num_versiculo)


def build_strong_request(diccionario_url):
    return LOGOS_URL + diccionario_url


def do_scraper(testamento, libro_Abrv, num_libro, num_versiculo):
    request = build_interlineal_request(
        testamento, libro_Abrv, num_libro, num_versiculo)
    response = do_request(request)
    soup = get_beautifulsoup(response)
    palabras = do_findall(soup, 'span', CLASS[testamento][0])
    tipos_palabra = do_findall(
        soup, 'span', CLASS[testamento][1])
    palabras_hebreo = do_findall(
        soup, 'span', CLASS[testamento][2])
    codigos_diccionario = do_select(soup, 'td a')
    return get_estructura(palabras, tipos_palabra, palabras_hebreo, codigos_diccionario)


def get_estructura(palabras, tipos_palabra, palabras_hebreo, codigos_diccionario):
    dic = {}
    for palabra, tipo_palabra, palabra_hebreo, codigo_diccionario in zip(palabras, tipos_palabra, palabras_hebreo, codigos_diccionario):
        estructura = {}
        estructura['tipo'] = tipo_palabra['title']
        estructura['hebreo'] = palabra_hebreo['title']
        estructura['codigo_diccionario'] = codigo_diccionario.string
        estructura['diccionario_url'] = build_strong_request(
            codigo_diccionario['href'])
        dic[palabra.string] = estructura
    return dic
