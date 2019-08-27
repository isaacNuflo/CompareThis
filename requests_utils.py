import requests
import json
from bs4 import BeautifulSoup

CLASS = {"NT": ["text-danger", "parsing cursor-pointer text-warning",
                "gw cursor-pointer greek-bold interl text-success"],
         "AT": ["text-danger translation-hebrew", "gw parsing cursor-pointer text-warning", 
         "gw cursor-pointer hebrew-ezra-bold interl text-success"]}


def get_beautifulsoup(response):
    return BeautifulSoup(response.text, 'html.parser')


def do_request(request):
    return requests.get(request)


def get_response_text(response):
    return json.loads(response.content.decode('utf-8'))["text"]


def do_findall(soup, element, class_):
    return soup.findAll(element, class_)


def do_select(soup, selector):
    return soup.select(selector)


def get_libros():
    with open('libros.json') as json_file:
        return json.load(json_file)
