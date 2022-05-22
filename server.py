# Script to connect to MySQL Server hosted on this box
# Listens to the incoming commections using socket module and connects to the MySQL using mysql module.
# Returns messages back to the client sending the querry.
# Optimize with multithreading to handle more than one client querries

import socket
from ProjectModules.ServerModules.server_modules import *

def main():
    """
    Main function. Calls other functions during run-time.
    """
    print("Create the initial server socket .....")
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Binding socket....")
    s.bind((HOST, PORT))
    print("Putting socket in listening state....")
    s.listen(1)

    # test_data()
    print("Get into while loop.....")
    while True:
        print("\nListening for incoming connections...\n")
        (clientsocket, address) = s.accept()
        print('\nConnected by', address)
        # messaging(clientsocket)
        Chat(clientsocket).messaging()

if __name__ == "__main__":
    main()

