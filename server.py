from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person


#GLOBAL VARIABLES
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZ = 1024



def broadcast():
    pass


def client_communication():
    """
    Thread to handle all messages from client
    :param client: Person
    :RETURN: None 
    """
 
    client = person.client
    name = person.name
    addr = person.addr
    while True:
        msg = person.recv(BUFSIZ)
        if msg == bytes("{quit}", "utf8"):
            client.close()
        else:
            pass


 



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
            person = Person(addr, client)
            print(f"[CONNECTION] {addr} connected to server at {time.time()}")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print("[FAILURE]")
            run = False

    print("SERVER CRASHED")

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)



if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS) #listen for 5 connections
    print("[STARTED] Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()





