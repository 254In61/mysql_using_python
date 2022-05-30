# Code to run test cases in Docker Containers
# Keeping all code including classes in one file to make it easier to copy to client users.Just 1 file client.py

import socket
import json
from ClientModules.client_modules import *
from common_vars import *


def main():

    """
    Main function. Calls other functions during run-time.
    """
    # Decide Table within the DB to be searched as first step
    # print("\n1 = Countries \n2 = Cars\n3 = Schools\n4 = Houses\n")
    # choice = input("Key in the database to be searched(1,2,3 or 4) as per the menu : ")

    # if choice not in ["1","2","3","4"]:
    #     print("Error. Key in the right value as per the instruction.")

    # else:
    #     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     client_socket.connect((HOST, PORT))
    #     if choice == "1":
    #         table_name = "countries:"
    #         print("\n1 = Search by country\n2 = Search by capitol\n3 = Search by head of state\n")
    #         search_id = input("Key in option(1,2,3) as per the menu : ")
            
    #         if search_id not in ["1","2","3"]:
    #             print("Wrong value entered. Value should be either 1,2 or 3 as per the menu.")

    #         else:
    #             if search_id == "1":
    #                 column_id = "country_name"

    #             elif search_id == "2":
    #                 column_id = "capitol"

    #             elif search_id == "3":
    #                 column_id = "head_of_state"

    #             search_name = input("Key in name[country,capitol or head of state] : ")
    #             print(Chat(create_query(table_name,column_id,search_name),client_socket).messaging())
    data1 = [
        ["countries","country_name","KeNya"],
        ["countries","country_name","cysaua"],
        ["countries","capitol","WASHIngton"],
        ["countries","capitol","W67snwsy"],
        ["countries","head_of_state","KAGame"],
        ["countries","head_of_state","K8jsuea"],
    ]
    
    for item in data1:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        table_name = item[0]
        column_id = item[1]
        search_name = item[2]

        print(Chat(create_query(table_name,column_id,search_name),client_socket).messaging())
    


if __name__ == "__main__":
    main()
