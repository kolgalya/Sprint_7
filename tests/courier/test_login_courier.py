from scooter_api import ScooterApi
from data import TestDataCreateCourier as TDCC
import help
import allure

class TestLoginCourier:
    @allure.description('Курьер может авторизоваться')
    def test_login_courier(self):
        body = TDCC.create_courier_body()
        courier = ScooterApi.create_courier(body)
        del body["firstName"]
        courier = ScooterApi.login_courier(body)
        assert courier.status_code == 200 and courier.json()["id"] != None

    @allure.description('Курьер не может авторизоваться без логина')
    def test_login_courier_without_login(self):
        body = TDCC.create_courier_body()
        courier = ScooterApi.create_courier(body)
        body["login"] = ""
        del body["firstName"]
        courier = ScooterApi.login_courier(body)
        assert courier.status_code == 400

    @allure.description('Курьер не может авторизоваться без пароля')
    def test_login_courier_without_password(self):
        body = TDCC.create_courier_body()
        courier = ScooterApi.create_courier(body)
        body["password"] = ""
        del body["firstName"]
        courier = ScooterApi.login_courier(body)
        assert courier.status_code == 400

    @allure.description('Курьер не может авторизоваться без корректного логина')
    def test_login_courier_without_login(self):
        body = TDCC.create_courier_body()
        courier = ScooterApi.create_courier(body)
        body["login"] = help.generate_random_string(4)
        del body["firstName"]
        courier = ScooterApi.login_courier(body)
        assert courier.status_code == 404

    @allure.description('Курьер не может авторизоваться без корректного пароля')
    def test_login_courier_without_login(self):
        body = TDCC.create_courier_body()
        courier = ScooterApi.create_courier(body)
        body["password"] = help.generate_random_string(6)
        del body["firstName"]
        courier = ScooterApi.login_courier(body)
        assert courier.status_code == 404