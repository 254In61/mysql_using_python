# Server modules
import mysql.connector
import json


mysql_host = "*****"
mysql_user = "*****"
mysql_password = "****"
mysql_db = "*****"


def mysql_info():
    return mysql_host,mysql_user,mysql_password,mysql_db

class DataBaseQuery():
    def __init__(self,in_str):
        self.in_str = in_str

    def process(self):

        try: 
            # Create mysql connection instance
            # Need to find a way to encrypt the password!
            mysql_host,mysql_user,mysql_password,mysql_db = mysql_info()
            sql_con = mysql.connector.connect( host = mysql_host, user = mysql_user,password = mysql_password,database = mysql_db)
            mycursor = sql_con.cursor()

            # Execute mysql querry after spliting the incoming message
            mycursor.execute("select * from countries where {} = '{}'".format(self.in_str.split(":")[0],self.in_str.split(":")[1]))
            output = mycursor.fetchall() # ==> <class 'list'>

            if output == []:
                return "ERROR.No data present"

            else:
                # Convert output to dictionary , then return as a json string.
                return json.dumps(
                    {
                        'country' : output[0][1], 
                        'capitol' : output[0][2],
                        'population' : output[0][3],
                        'head_of_state' : output[0][4]
                    }
                    )
        
        except IndexError:
            return "ERROR during data querry"

        # except:
        #     return "ERROR during data querry"


class Chat():
    """
    Class that perfoms chatting i,e send recieve of messages through the created socket.
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
        print(query_result)
        self.clientsocket.sendall(query_result.encode("utf-8"))

        return query_result # Here for unit testing purpose.Class perfoms the work end to end.
