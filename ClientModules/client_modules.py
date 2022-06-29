import socket
import json

# Client re-usable modules
HOST = '192.168.1.92' # Server's IP address..Can be resolved using gethostbyname() if using DNS.
PORT = 50055   # Arbitrary non-privileged port
class Chat():
    """
    Class that handles chat.
    Gets input from CreateQuery class for the query to send.
    """
    def __init__(self,query,client_socket):
        self.query = query
        self.client_socket = client_socket
        
    def messaging(self):
        # Method to perform the messaging with server
        
        # Send query to server through socket
        self.client_socket.sendall(self.query.encode("utf-8"))

        # Recieve result from server
        query_result = self.client_socket.recv(1024).decode("utf-8")
        return query_result

def perform_query(query):

    print("Query : ",query)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    return Chat(query,client_socket).messaging()

    

     
    