import random
import requests


class Api():
    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    def login(self, password, username):
        data = {"password": password, "username": username}
        return self._s.post(self.host + "/api/v1/auth/sign_in", json=data)

    def authorize(self, username, password):
        res = self.login(username, password)
        if res.status_code != 200:
            raise Exception("Unable to authorize using given credentials")
        session_token = res.json().get("token")
        cookie = requests.cookies.create_cookie("token", session_token)
        self._s.cookies.set_cookie(cookie)

    def randome(self):
        return random.random()

    def payment_from(self):
        json = {
            "amount": 10,
            "currency_code": "CAD",
            "customer_fee_percent": 0,
            "customer_id": "test",
            "customer_profile": {
                "address_a": "string",
                "address_b": "string",
                "city": "string",
                "country": "string",
                "date_of_birth": "string",
                "email": "string",
                "first_name": "string",
                "id": 0,
                "last_name": "string",
                "phone": "string",
                "postal_code": "string",
                "province": "string",
                "sin": "string"
            },
            "locale": "NA",
            "params": [
                "string"
            ],
            "redirect_url": {
                "failed_url": "string",
                "success_url": "string"
            },
            "transaction_id": f"{self.randome()}"
        }
        return json

    def headers(self):
        headers = {"MerchantToken": "goodtry", "MerchantID": "Merchant-CA-1"}
        return headers

    def send_to_customer_defined(self):
        json = {
            "amount": 10,
            "currency_code": "CAD",
            "customer_fee_percent": 100,
            "customer_id": "test",
            "customer_profile": {
                "address_a": "string",
                "address_b": "string",
                "city": "string",
                "country": "string",
                "date_of_birth": "string",
                "email": "string",
                "first_name": "string",
                "id": 0,
                "last_name": "string",
                "phone": "string",
                "postal_code": "string",
                "province": "string",
                "sin": "string"
            },
            "locale": "NA",
            "notification_type": "EMAIL",
            "params": [
                "string"
            ],
            "redirect_url": {
                "failed_url": "string",
                "success_url": "string"
            },
            "transaction_id": f"{self.randome()}"
        }
        return json

    def send_to_not_verified(self):
        json = {
            "amount": 10,
            "bank_account": {
                "account_branch": "00012",
                "account_institution": "343",
                "account_number": "string",
                "account_routing": "string"
            },
            "country_code": "CA",
            "currency_code": "CAD",
            "customer_fee_percent": 100,
            "customer_id": "test",
            "customer_profile": {
                "address_a": "string",
                "address_b": "string",
                "city": "string",
                "country": "string",
                "date_of_birth": "string",
                "email": "string",
                "first_name": "string",
                "id": 0,
                "last_name": "string",
                "phone": "string",
                "postal_code": "string",
                "province": "string",
                "sin": "string"
            },
            "locale": "NA",
            "params": [
                "string"
            ],
            "transaction_id": f"{self.randome()}"
        }
        return json

    def send_to_verified(self):
        json = {
            "amount": 10,
            "currency_code": "CAD",
            "customer_fee_percent": 100,
            "customer_id": "test",
            "locale": "NA",
            "params": [
                "string"
            ],
            "transaction_id": f"{self.randome()}"
        }
        return json

#response_body = response.json()
#assert len(response_body["places"]) == 1#