import requests
from pages.api import Api
import pytest


@pytest.mark.smoke
class TestApiMerchantBalanceController():
    def test_get_balance(self):
        self.link = "https://test.banksend.com/api/v1/balance"
        api = Api(self)
        response = requests.get(self.link, headers=api.headers())
        print(f"\n{response.status_code}")
        response_body = response.json()
        print(response.text)
        assert response.status_code == 200, "Status code for GetBalance != 200"


@pytest.mark.smoke
class TestApiMerchantTransactionController():
    def test_payment_form(self):
        api = Api(self)
        self.link = "https://test.banksend.com/api/v1/transactions/incoming/payment_form"
        response = requests.post(self.link, headers=api.headers(), json=api.payment_from())
        print(f"\n{response.status_code}")
        print(response.text)
        assert response.status_code == 200, "Status code for payment form != 200"

    def test_transaction_list(self):
        api = Api(self)
        self.link = "https://test.banksend.com/api/v1/transactions/list"
        response = requests.get(self.link, headers=api.headers())
        #        print(response.text)
        print(f"\n{response.status_code}")
        assert response.status_code == 200, "Transaction list not available"

    def test_send_to_customer_defined(self):
        api = Api(self)
        self.link = "https://test.banksend.com/api/v1/transactions/outgoing/send_to_customer_defined"
        response = requests.post(self.link, headers=api.headers(), json=api.send_to_customer_defined())
        print(f"\n{response.status_code}")
        print(response.text)
        assert response.status_code == 200, "Status code for customer defined != 200"

    def test_send_to_not_verified(self):
        self.link = "https://test.banksend.com/api/v1/transactions/outgoing/send_to_verified"
        api = Api(self)
        response = requests.post(self.link, headers=api.headers(), json=api.send_to_not_verified())
        print(f"\n{response.status_code}")
        assert response.status_code == 200, "Status code for not verified != 200"

    def test_send_to_verified(self):
        self.link = "https://test.banksend.com/api/v1/transactions/outgoing/send_to_verified"
        api = Api(self)
        response = requests.post(self.link, headers=api.headers(), json=api.send_to_verified())
        print(f"\n{response.status_code}")
        assert response.status_code == 200, "Status code for to verified != 200"


@pytest.mark.smoke
class TestAuthenticationController():
    def test_login(self):
        api = Api("https://test.banksend.com")
        password = "12345678"
        username = "superadmin-test@banksend.com"
        _r = api.login(password, username)
        print(f"\n{_r.status_code}")
        assert _r.status_code == 200, "Status code != 200 when user trying to log in"
