import json
from requests import Response
class Checking():
    
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Success, status code: ", response.status_code)
        else:
            print("fail")
            
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("all tokens here")
        
    @staticmethod 
    def generate_json_tokens(response: Response):
        token = json.loads(response.text)
        return list(token)
    
    @staticmethod
    def check_json_value(response: Response, field_name, search_string):
        check = response.json()
        check_info = check.get(field_name)
        if search_string in check_info:
            print(field_name + " has correct value")
        else:
            print(field_name + " has wrong value")
            