from cgi import test
import datetime
import os
from requests import Response

class Logger():
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d")) + ".log"
    
    @classmethod
    def write_log(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)
    
    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        
        data = f"\n------\n"
        data += f"Test: {test_name}\n"
        data += f"Time: {str(datetime.datetime.now())}\n"
        data += f"Request method:{method}\n"
        data += f"Request URL:{url}\n"
        
        cls.write_log(data)
        
    @classmethod
    def add_response(cls, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)
        
        data = f"Response code: {result.status_code}\n"
        data += f"Response text: {result.text}\n"
        data += f"Response headers: {headers_as_dict}\n"
        data += f"Response cookies: {cookies_as_dict}\n"
        data += f"\n------\n"
        print(data)
        cls.write_log(data)