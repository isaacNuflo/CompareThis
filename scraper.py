import requests
from requests_utils import do_request, get_beautifulsoup, do_findall, do_select

LOGOS_URL = 'https://logosklogos.com/'
INTERLINEAL_URL = 'interlinear/{}/{}'
STRONG_URL = 'strong_hebrew/{}'


def build_interlineal_request(testamento, libro_Abrv):
    return LOGOS_URL + INTERLINEAL_URL.format(testamento, libro_Abrv)


def build_strong_request(codigo_diccionario):
    return LOGOS_URL + STRONG_URL.format(codigo_diccionario)


def do_scraper(testamento, libro_Abrv):
    request = build_interlineal_request(testamento, libro_Abrv)
    response = do_request(request)
    soup = get_beautifulsoup(response)
    palabras = do_findall(soup, 'span', 'text-danger translation-hebrew')
    tipos_palabra = do_findall(
        soup, 'span', 'gw parsing cursor-pointer text-warning')
    palabras_hebreo = do_findall(
        soup, 'span', 'gw cursor-pointer hebrew-ezra-bold interl text-success"')
    codigos_diccionario = do_select(soup, 'td a')
    return get_estructura(palabras, tipos_palabra, palabras_hebreo, codigos_diccionario)


def get_estructura(palabras, tipos_palabra, palabras_hebreo, codigos_diccionario):
    dic = {}
    for palabra, tipo_palabra, palabra_hebreo, codigo_diccionario in zip(palabras, tipos_palabra, palabras_hebreo, codigos_diccionario):
        estructura = {}
        estructura['tipo'] = tipo_palabra['title']
        estructura['hebreo'] = palabra_hebreo['title']
        estructura['codigo_diccionario'] = codigo_diccionario['href']
        estructura['diccionario_url'] = build_strong_request(
            codigo_diccionario['href'])
        print(estructura)
        dic[palabra.string] = estructura
    print(dic)
    return dic
