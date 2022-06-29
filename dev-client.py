
# Dev script that is run during development and will be run by the Docker containers as intergration tests

import socket
import json
from ClientModules.client_modules import *

def main():

    """
    Main function. Calls other functions during run-time.
    """
    test_data = ["name:Kenya","capital:Kampala","name:Usa","capital:Canberra","name:ujsh23","capital:xshs31"]
    for query in test_data:
        print(perform_query(query))


if __name__ == "__main__":
    main()




