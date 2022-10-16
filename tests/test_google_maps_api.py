from utils.api import Google_maps_api
from requests import Response
from utils.checking import Checking

class Test_create_place():
    def test_create_new_place(self):
        
        print("Post method")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        fields_post = Checking.generate_json_tokens(result_post)
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, fields_post)
        Checking.check_json_value(result_post, 'status', 'OK')
        
        print("GET method (for post)")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        fields_get = Checking.generate_json_tokens(result_get)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, fields_get)
        
        print("PUT method")
        result_put: Response = Google_maps_api.put_new_place(place_id)
        fields_put = Checking.generate_json_tokens(result_put)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, fields_put)
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')
        
        print("GET method (for PUT)")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        fields_get = Checking.generate_json_tokens(result_get)
        Checking.check_json_token(result_get, fields_get)
        Checking.check_status_code(result_get, 200)
        
        print("DELETE method")
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        fields_delete = Checking.generate_json_tokens(result_delete)
        Checking.check_json_token(result_delete, fields_delete)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_value(result_delete, 'status', 'OK')
        
        print("GET method (for DELETE)")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        fields_get = Checking.generate_json_tokens(result_get)
        Checking.check_json_token(result_get, fields_get)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_value(result_get, 'msg', 'Delete operation failed')