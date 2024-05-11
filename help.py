import random
import string
import allure

@allure.step('Генерируем случайную строку')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Генерируем случайный логин, пароль и имя курьера')
def create_courier_body():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    CREATE_COURIER_BODY = {
        "login": login,
        "password": password,
        "firstName": first_name
        }
    return CREATE_COURIER_BODY

@allure.step('Данные для оформления заказа')
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
