def compare():
    if args.versiculo:
        libro = re_search(REGEX_LIBRO, args.versiculo)
        cita = re_search(REGEX_CITA, args.versiculo)
        if libro and cita:
            texto = do_request()
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


def do_request(cita):
    libro_ingles = libros.get(libro, "")
    cita = cita.replace(":", ".")
    request = URL_API.format(libro_ingles + cita, API_KEY)
    response = requests.get(request)

    return json.loads(response.content.decode('utf-8'))["text"]


def re_search(regex, cadena):
    return re.search(regex, cadena).group(0)
