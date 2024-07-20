import os
from src.ping_test import check_ping
def test_ping():
    status = check_ping("google.com")
    if status ==  "Network Active" or status == "Network Error":
        assert True
    else:
        assert False
        
    status = check_ping("no_name")
    if status == "Network Active" or status == "Network Error":
        assert True
    else:
        assert False