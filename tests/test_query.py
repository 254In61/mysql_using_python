# Client modules testing

import socket
import pytest
from ClientModules.client_modules import *

# Test CreateQuery class

def test_query_country_name():
    # Testing query by country name
    # Expected to suceed
    assert perform_query("name:Kenya") == '[254, "Kenya", "Nairobi", "Uhuru Kenyatta", 60000000]'

def test_query_country_name_Error():
    # Testing create_query() function
    assert perform_query("name:Yuvswm") == "ERROR.No data present"

def test_query_capital_city():
    # Testing query by country name
    # Expected to suceed
    assert perform_query("capital:Washington") == '[1, "Usa", "Washington", "Joe Biden", 365000000]'

def test_query_capital_city_Error():
    # Testing query by country name
    # Expected to suceed
    assert perform_query("capital:Wysu73sz") == "ERROR.No data present"


