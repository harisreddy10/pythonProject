from socket import *


def createServer():
    serverskt = socket(AF_INET, SOCK_STREAM)

    try:
        serverskt.bind(('localhost', 9212))
        serverskt.listen(5)
        print('Server is listening on http://localhost:9212')

        while True:
            (client_skt, address) = serverskt.accept()
            request_data = client_skt.recv(5000).decode()
            request_lines = request_data.split("\n")

            if len(request_lines) > 0:
                print(request_lines[0])

            # HTML content with the correct heading
            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += '<html><body><h1>Hello World</h1></body></html>\r\n\r\n'

            client_skt.sendall(data.encode())
            client_skt.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serverskt.close()


createServer()
