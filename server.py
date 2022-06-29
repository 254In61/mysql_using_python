# Server side script
import socket
import mysql.connector
import json
import os


HOST = '192.168.1.92' # Server's IP address..Can be resolved using gethostbyname() if using DNS.
PORT = 50055   # Arbitrary non-privileged port


def connect_mysql():
    return mysql.connector.connect( host = "localhost", user = os.environ.get('MYSQL_USER'),password = os.environ.get('MYSQL_PASSWORD'),database = "mydb")

class DataBaseQuery():
    """
    - A query comes in as a string value 'column_name:value_searched'
    - Query is split into the different values to fit into an sql WHERE format type.
    - Results are converted into JSON string before returned.
    """
    def __init__(self,in_str):
        self.in_str = in_str

    def process(self):

        try: 
            sql_con = connect_mysql()
            mycursor = sql_con.cursor()

            query = "select * from countries where {} = '{}'".format(self.in_str.split(":")[0],self.in_str.split(":")[1])
            print("Query : ",query)
            mycursor.execute(query)
            output = mycursor.fetchall()
            print("Results from MySQL Server : ",output)

            if output == []:
                out_string = "ERROR.No data present"

            else:
                out_string = json.dumps(output[0])
            
            print("Results sent to client : ",out_string)
            return out_string

        except IndexError:
            return "ERROR during data querry"

class Chat():
    """
    - Job of class is just to send and recieve messages from client through the created socket.
    """
    def __init__(self,clientsocket):
        self.clientsocket = clientsocket

    def messaging(self):
        """
        Step 1: Decode query message recieved through clientsocket.
        Step 2: Query the MySQL server through DBQuerry class
        Step 3: Send query results back to client.
        """
        query = self.clientsocket.recv(1024).decode("utf-8")
        print("Client query : ",query)
        query_result = DataBaseQuery(query).process()
        self.clientsocket.sendall(query_result.encode("utf-8"))

        return query_result


def main():
    print("Create the initial server socket .....")
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Binding socket....")
    s.bind((HOST, PORT))
    print("Putting socket in listening state....")
    s.listen(1)

    # test_data()
    print("Get into while loop.....")
    while True:
        # Server socker role is just to create client socket & Client socket handles the exchange between client and server.
        print("\nListening for incoming connections...")
        (clientsocket, address) = s.accept()
        print('\nSuccessfull connection to : ', address)
        # messaging(clientsocket)
        Chat(clientsocket).messaging()

if __name__ == "__main__":
    main()

