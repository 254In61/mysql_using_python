# Client modules testing

import socket
import pytest
from ProjectModules.ClientModules.client_modules import *

# Test CreateQuery class

def test_client_CreateQuery_country_name():
    # Testing create_query() function
    assert CreateQuery("1","Kenya").get_string() == "country_name:Kenya"

def test_client_CreateQuery_capitol():
    # Testing create_query() function
    assert CreateQuery("2","Dar").get_string() == "capitol:Dar"

def test_client_CreateQuery_head_of_state():
    # Testing create_query() function
    assert CreateQuery("3","Biden").get_string() == "head_of_state:Biden"

# Test Chat class
# Helper
def create_socket():
    """
    Needed. There has to be a new socket created for each test case.
    The socket closes once message is sent and feedback recieved. It is not persistent.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    return client_socket

# Test Cases

def test_client_Chat_country_name():
    # Test Country search
    client_socket = create_socket()
    assert Chat("country_name:Tanzania",client_socket).messaging() == '{"country": "Tanzania", "capitol": "Dar", "population": 65, "head_of_state": "Suluhu"}'

def test_client_Chat_capitol():
    # Test Country search
    client_socket = create_socket()
    assert Chat("capitol:Nairobi",client_socket).messaging() == '{"country": "Kenya", "capitol": "Nairobi", "population": 60, "head_of_state": "Uhuru"}'

def test_client_Chat_head_of_state():
    # Test Country search
    client_socket = create_socket()
    assert Chat("head_of_state:Biden",client_socket).messaging() == '{"country": "USA", "capitol": "Washington", "population": 365, "head_of_state": "Biden"}'


