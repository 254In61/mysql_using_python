
import socket
import json
from ClientModules.client_modules import *


def main():

    """
    Main function. Calls other functions during run-time.
    """
    # Decide Table within the DB to be searched as first step
    print("\nMENU\n1 = Search by country name\n2 = Search by country capital\n")
    choice = input("Key in search criteria as per the menu : ")

    if choice not in ["1","2"]:
        print("Error. Key in the right value as per the menu.")

    else:

        if choice == "1":
            column_id = "name"

        elif choice == "2":
            column_id = "capital"

        query = column_id + ":" + input("Key in value : ").capitalize()
        print(perform_query(query))

if __name__ == "__main__":
    main()
