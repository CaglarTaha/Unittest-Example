import unittest
import requests
import json


class UnittestForHomeWork(unittest.TestCase):

    #Extra Example Google REQUEST 
    def test_valid_url(self):
        self.assertEqual(200,requests.get('http://www.google.com/search'))

    # API 1: Get All Products List
    def test_get(self):
        response = requests.get("https://automationexercise.com/api/productsList")
        print(response.text)
# API 2: POST To All Products List

    def test_post(self):
        payload = {"key1": "value1"}
        send = requests.post(
            "https://automationexercise.com/api/productsList", data=payload)
        print(send.status_code)
# API 3: Get All Brands List

    def test_get2(self):
        payload = {"key1": "value1"}
        response = requests.post(
            "https://automationexercise.com/api/brandsList", data=payload)
        print(response.text)
        print(response.status_code)

    def test_get3(self):
        response = requests.get(
            "https://automationexercise.com/api/brandsList")
        body = json.loads(response.text)
        item_id = body["brands"][1]["id"]
        self.assertEqual(2, item_id)

# API 4: PUT To All Brands List
    def test_put(self):
        params = {"search_product": "top"}
        Send = requests.put(
            "https://automationexercise.com/api/brandsList", data=params)
        body = json.loads(Send.text)
        print(body)
# API 5: POST To Search Product

    def test_post3(self):
        api_url = "https://automationexercise.com/api/searchProduct"
        request_data = {"search_product": "top"}
        response = requests.post(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        content = json.loads(response.text)
        self.assertEqual(
            "Tops", content["products"][0]["category"]["category"])
# 6

    def test_post4(self):
        api_url = "https://automationexercise.com/api/verifyLogin"
        request_data = {"email": "mtaha.mtal@gmail.com"}
        response = requests.post(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)
# 7

    def test_delete(self):
        api_url = "https://automationexercise.com/api/verifyLogin"
        request_data = {"email": "mtaha.mtal@gmail.com"}
        response = requests.delete(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)
# 8

    def test_api_create_account_test_post_6(self):
        api_url = "https://automationexercise.com/api/createAccount"
        request_data = {
            "name": "Taha Caglar",
            "email": "mtaha.mtal@gmail.com",
            "password": "secure_password",
            "title": "Mr",
            "birth_date": "01",
            "birth_month": "01",
            "birth_year": "2001",
            "firstname": "Taha",
            "lastname": "Cahlar",
            "company": "Codativ",
            "address1": "adress",
            "address2": "Apt A2",
            "country": "Turkey",
            "zipcode": "3400",
            "state": "Istanbul",
            "city": "Istanbul",
            "mobile_number": "232342342"
        }

        response = requests.post(api_url, data=request_data)

        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)
# 9

    def test_api_delete2(self):
        api_url = "https://automationexercise.com/api/deleteAccount"
        request_data = {"email": "mtaha.mtal@gmail.com", 'password': '12345'}
        response = requests.delete(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)
# 10

    def test_api_delete3(self):
        api_url = "https://automationexercise.com/api/deleteAccount"
        request_data = {"email": "mtaha.mtal@gmail.com", 'password': '12345'}
        response = requests.delete(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)
# 11

    def test_api_put2(self):
        api_url = "https://automationexercise.com/api/updateAccount"
        request_data = {
            "name": "Muhammed Taha Caglar",
            "email": "mtaha.mtal@gmail.com",
            "password": "secure_password",
            "title": "Mr",
            "birth_date": "01",
            "birth_month": "10",
            "birth_year": "2001",
            "firstname": "Taha",
            "lastname": "Caglar",
            "company": "Codativ",
            "address1": "Adress",
            "address2": "Apt A2",
            "country": "Turkey",
            "zipcode": "3400",
            "state": "Istanbul",
            "city": "Istanbul",
            "mobile_number": "232342342"
        }

        response = requests.put(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)
# 13

    def test_api_get4(self):
        api_url = "https://automationexercise.com/api/getUserDetailByEmail"
        request_data = {"email": "mtaha.mtal@gmail.com"}
        response = requests.delete(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)


if __name__ == '__main__':
    unittest.main()
