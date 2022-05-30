# Testing DataBaseQuery module
from ServerModules.server_modules import *
# from ProjectModules.common_vars import HOST,PORT

# Test DataBaseQuery Cases

def test_server_DataBaseQuery_country_name():
    # Test Country search
    assert DataBaseQuery("countries:country_name:Tanzania").process() == '["Tanzania", "Dar", 65, "Suluhu"]'

def test_server_DataBaseQuery_capitol():
    # Test capitol search
    assert DataBaseQuery("countries:capitol:Nairobi").process() == '["Kenya", "Nairobi", 60, "Uhuru"]'

def test_server_DataBaseQuery_head_of_state():
    # Test head of state
    assert DataBaseQuery("countries:head_of_state:Biden").process() == '["USA", "Washington", 365, "Biden"]'


# Test Chat Cases