from scooter_api import ScooterApi
from data import TestDataCreateCourier as TDCC
import help
import allure

class TestCreateCourier:
    @allure.description('Курьера можно создать')
    def test_can_create_courier(self):
        body = TDCC.create_courier_body()
        courier = ScooterApi.create_courier(body)
        assert courier.status_code == 201 and courier.json() == {'ok': True}

    @allure.description('Нельзя создать двух курьеров с одинаковым логином')
    def test_cannot_create_identical_couriers(self):
        body = TDCC.create_courier_body()
        courier = ScooterApi.create_courier(body)
        body["password"] = help.generate_random_string(10)
        body["firstName"] = help.generate_random_string(10)
        courier_2 = ScooterApi.create_courier(body)
        assert courier_2.status_code == 409

    @allure.description('Можно создать курьера без необязательного поля "Имя"')
    def test_can_create_courier_without_name(self):
        body = TDCC.create_courier_body()
        body["firstName"] = ''
        courier = ScooterApi.create_courier(body)
        assert courier.status_code == 201 and courier.json() == {'ok': True}

    @allure.description('Нельзя создать курьера без обязательного поля "Логин"')
    def test_cannot_create_courier_without_login(self):
        body = TDCC.create_courier_body()
        body["login"] = ''
        courier = ScooterApi.create_courier(body)
        assert courier.status_code == 400

    @allure.description('Нельзя создать курьера без обязательного поля "Пароль"')
    def test_cannot_create_courier_without_password(self):
        body = TDCC.create_courier_body()
        body["password"] = ''
        courier = ScooterApi.create_courier(body)
        assert courier.status_code == 400
