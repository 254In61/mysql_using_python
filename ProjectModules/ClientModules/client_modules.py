# Client modules and functions
import socket
import json

HOST = '192.168.1.111' # Server's IP address..Can be resolved using gethostbyname() if using DNS.
PORT = 50003   # Arbitrary non-privileged port

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

class CreateQuery():
    def __init__(self,search_id,my_value):
        self.search_id = search_id
        self.my_value = my_value

    def get_string(self):
        if self.search_id == "1":
            key_id = "country_name"
        
        elif self.search_id == "2":
            key_id = "capitol"

        elif self.search_id == "3":
            key_id = "head_of_state"

        query = key_id + ":" + self.my_value

        return query 