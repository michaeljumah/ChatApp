from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


BUFSIZ = 1024


def client_communication(client):
    run = True 
    while run:
        msg = client.recv(BUFSIZ)
        if msg == bytes("{quit}", "utf8"):
            client.close()
        else:






def wait_for_connection(SERVER):
    """
    wait for connection from new client, start new tread once connected
    :param SERVER:SOCKET
    :return:None
    """
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            Thread(target=client_communication, args=(client,)).start()
        except Exception as e:
            print("[FAILURE]")
            run = false




#GLOBAL VARIABLES
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)



if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS) #listen for 5 connections
    print("[STARTED] Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection, (SERVER))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()





