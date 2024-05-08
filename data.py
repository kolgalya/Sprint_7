import allure
import help

class TestDataCreateCourier:
    @allure.step('Генерируем случайный логин, пароль и имя курьера')
    def create_courier_body():
        login = help.generate_random_string(10)
        password = help.generate_random_string(10)
        first_name = help.generate_random_string(10)
        CREATE_COURIER_BODY = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return CREATE_COURIER_BODY

class TestDataCreateOrder:
    @allure.step('Генерируем случайный логин, пароль и имя курьера')
    def create_order_body(color):
        ORDER_BODY = {
        "firstName": "Jon",
        "lastName": "Snow",
        "address": "Winterfell, north tower",
        "metroStation": 13,
        "phone": "+7 800 131 13 13",
        "rentTime": 5,
        "deliveryDate": "2026-06-06",
        "comment": "Winter is coming"
        }
        if color!= '':
            ORDER_BODY["color"] = color
        else:
            ORDER_BODY
        return ORDER_BODY
