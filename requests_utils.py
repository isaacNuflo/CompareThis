import requests
import json
from bs4 import BeautifulSoup

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