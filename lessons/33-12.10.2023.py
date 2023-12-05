# Паттерн MVC - это шаблон программирования, который позволяет разделять логику приложения на три части:
# Model - обработка данных и логика приложения
# View (вид или представление) - предоставление данных пользователю в любом поддерживаемом виде
# Controller - обработка запросов пользователя и вызов соответствующих ресурсов


# Сокеты

import socket
from veiw import index
from veiw import blog


URLS = {
    '/': index,
    '/blog': blog
}


def parse_request(request):
    parse = request.split()
    method = parse[0]
    url = parse[1]
    return method, url


def generate_headers(method, url):
    if method != 'GET':
        return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
    if url not in URLS:
        return 'HTTP/1.1 404 Page Not Found!\n\n', 404
    return 'HTTP/1.1 200 OK!\n\n', 200


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><h3>Page Not Found!</h3>'
    elif code == 405:
        return '<h1>405</h1><h3>Method Not Allowed!</h3>'
    return URLS[url]()


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)  # URLS.get(url, 'Errors 404')
    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))  # 127.0.0.1:5000
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(f'Клиент {addr} => \n{request.decode("utf-8")}\n')

        response = generate_response(request.decode())
        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    run()
