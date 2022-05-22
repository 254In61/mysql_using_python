# Code to run test cases in Docker Containers
import socket
from  ProjectModules.ClientModules.client_modules import *

def main():

    """
    Main function. Calls other functions during run-time.
    """
    # print("\n1 = Search by country\n2 = Search by capitol\n3 = Search by head of state\n")
    # search_id = input("Key in option(1,2,3) as per the menu : ")
    # # search_id = "2"
     
    # if search_id not in ["1","2","3"]:
    #     print("Wrong value entered. Value should be either 1,2 or 3 as per the menu.")

    # else:
    #     my_value = input("Key in name[country,capitol or head of state] : ").capitalize()
    #     # my_value = "Kigali"
        
    #     # Output will be in JSON string format. Client can play with the data from there.
    #     # my_value capitalized since the DB is stored as names with 1st character as capital
    
    data = [["1","Kenya"],["2","Washington"],["3","Suluhu"]]

    for item in data:
        search_id = item[0]
        my_value = item[1]
        query = CreateQuery(search_id,my_value).get_string()
        print(query)

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        query_result = Chat(query,client_socket).messaging()
        print(query_result)

if __name__ == "__main__":
    main()
