# Server modules
import mysql.connector
import json
from common_vars import *

mysql_host = "localhost"
mysql_user = "root"
mysql_password = "Ccie@2013"
mysql_db = "mydb"


def mysql_info():
    return mysql_host,mysql_user,mysql_password

class DataBaseQuery():
    """
    - Avoiding anything fancy in this class.
    - Simple, a query comes in as a string value 'table_name:column_name:value_searched'
    - Query is split into the different values to fit into an sql WHERE format type.
    - Results are converted into JSON string before returned.
    """
    def __init__(self,in_str):
        self.in_str = in_str

    def process(self):

        try: 
            # Create mysql connection instance
            # Need to find a way to encrypt the password!
            mysql_host,mysql_user,mysql_password = mysql_info()
            sql_con = mysql.connector.connect( host = mysql_host, user = mysql_user,password = mysql_password,database = mysql_db)
            mycursor = sql_con.cursor()

            # Execute mysql querry after spliting the incoming message
            query = "select * from {} where {} = '{}'".format(self.in_str.split(":")[0],self.in_str.split(":")[1],self.in_str.split(":")[2])
            print("Query : ",query)
            mycursor.execute(query)
            output = mycursor.fetchall()

            if output == []:
                out_string = "ERROR.No data present"

            else:
                # Avoiding first value which is not needed and the last value.
                # Avoiding Datetime bacause of 'TypeError: Object of type datetime is not JSON serializable'
                out_string = json.dumps(output[0][1:-1])
            
            print("Results from MySQL Server : ",output)
            print("Results sent to client : ",out_string)
            return out_string

        except IndexError:
            return "ERROR during data querry"

        # except:
        #     return "ERROR during data querry"


class Chat():
    """
    - Nothing fancy in this class. Job of class is just to send and recieve messages from client.
    - Class that perfoms chatting i,e send recieve of messages through the created socket.
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
        query_result = DataBaseQuery(query).process()
        self.clientsocket.sendall(query_result.encode("utf-8"))

        return query_result # Here for unit testing purpose.Class perfoms the work end to end.
