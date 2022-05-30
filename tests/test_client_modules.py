# Client modules testing

import socket
import pytest
from common_vars import HOST,PORT
from ClientModules.client_modules import *

# Test CreateQuery class

def test_client_create_query_country_name():
    # Testing create_query() function
    table_name = "countries"
    column_id = "country_name"
    search_name = "KeNYa"
    assert create_query(table_name,column_id,search_name) == "countries:country_name:Kenya"

def test_client_create_query_country_name_Error():
    # Testing create_query() function
    table_name = "countries"
    column_id = "country_name"
    search_name = "z45yy"
    assert create_query(table_name,column_id,search_name) == "countries:country_name:Z45yy" #value to be capitalized

def test_client_create_query_capitol():
    # Testing create_query() function
    table_name = "countries"
    column_id = "capitol"
    search_name = "DaR"
    assert create_query(table_name,column_id,search_name) == "countries:capitol:Dar"

def test_client_create_query_capitol_Error():
    # Testing create_query() function
    table_name = "countries"
    column_id = "capitol"
    search_name = "vv892v7"
    assert create_query(table_name,column_id,search_name) == "countries:capitol:Vv892v7" # Value to be capitalized

def test_client_create_query_head_of_state():
    # Testing create_query() function
    table_name = "countries"
    column_id = "head_of_state"
    search_name = "BIDEN"
    assert create_query(table_name,column_id,search_name) == "countries:head_of_state:Biden"

def test_client_create_query_head_of_state_Error():
    # Testing create_query() function
    table_name = "countries"
    column_id = "head_of_state"
    search_name = "ue78uyu"
    assert create_query(table_name,column_id,search_name) == "countries:head_of_state:Ue78uyu" # Value to be capitalized


# Helper
def create_socket():
    """
    Needed. There has to be a new socket created for each test case.
    The socket closes once message is sent and feedback recieved. It is not persistent.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    return client_socket

def test_client_Chat_country_name():
    # Test Country search
    query = "countries:country_name:Kenya"
    assert Chat(query,create_socket()).messaging() == '["Kenya", "Nairobi", 60, "Uhuru"]'

def test_client_Chat_country_name_Error():
    # Test Country search
    query = "countries:country_name:y78wus"
    assert Chat(query,create_socket()).messaging() == 'ERROR.No data present'

def test_client_Chat_capitol():
    # Test capitol search
    query = "countries:capitol:Nairobi"
    assert Chat(query,create_socket()).messaging() == '["Kenya", "Nairobi", 60, "Uhuru"]'

def test_client_Chat_capitol_Error():
    # Test capitol search
    query = "countries:capitol:yu9s0w"
    assert Chat(query,create_socket()).messaging() == 'ERROR.No data present'

def test_client_Chat_head_of_state():
    # Test head_of_state search
    query = "countries:head_of_state:Biden"
    assert Chat(query,create_socket()).messaging() == '["USA", "Washington", 365, "Biden"]'

def test_client_Chat_head_of_state():
    # Test head_of_state search
    query = "countries:head_of_state:ut921ms"
    assert Chat(query,create_socket()).messaging() == 'ERROR.No data present'


