# Client re-usable modules
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

def create_query(table_name,column_id,search_name):
    return table_name + ":" + column_id + ":" + search_name.capitalize()

     
    