# Testing DataBaseQuery module
from ProjectModules.ServerModules.server_modules import *


# Test DataBaseQuery Cases

def test_server_DataBaseQuery_country_name():
    # Test Country search
    assert DataBaseQuery("country_name:Tanzania").process() == '{"country": "Tanzania", "capitol": "Dar", "population": 65, "head_of_state": "Suluhu"}'

def test_server_DataBaseQuery_capitol():
    # Test capitol search
    assert DataBaseQuery("capitol:Nairobi").process() == '{"country": "Kenya", "capitol": "Nairobi", "population": 60, "head_of_state": "Uhuru"}'

def test_server_DataBaseQuery_head_of_state():
    # Test head of state
    assert DataBaseQuery("head_of_state:Biden").process() == '{"country": "USA", "capitol": "Washington", "population": 365, "head_of_state": "Biden"}'


# Test Chat Cases