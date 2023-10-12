from socket import *
def createServer():
    serverskt=socket(AF_INET,SOCK_STREAM)
    try:
        serverskt.bind(('localhost',9211))
        serverskt.listen(5)
        while(1):
            (clienskt,address)=serverskt.accept()
            rd=clienskt.recv(5000).decode()
            piecesURL=rd.split("\n")
            if(len(piecesURL)>0):print(piecesURL[0])

            #data to be tranmistted and for the server
            data='HTTP/1.1 200 OK\r\n'
            data+="Content-Type: text/html; charset=utf-8\r\n"
            data+="\r\n"
            data+="<html><body><h1><Hello World></h1></body></html>\r\n\r\n"
            clienskt.sendall(data.encode())
            clienskt.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...\n");
    except Exception as exc:
        print("Error:\n");
        print(exc)

    serverskt.close()
print('Access http://localhost:9211')
createServer()

