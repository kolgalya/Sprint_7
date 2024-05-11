import requests
import urls
import allure

class ScooterApi:
    @allure.step('Создание курьера: POST /api/v1/courier')
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER, json = body)

    @allure.step('Авторизация курьера: POST /api/v1/courier/login')
    def login_courier(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER, json = body)

    @allure.step('Удаление курьера: DELETE /api/v1/courier/:id')
    def delet_courier(id):
        return requests.delete(urls.BASE_URL + urls.CREATE_COURIER, json=id)

    @allure.step('Создание заказа: POST /api/v1/orders')
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER, json=body)

    @allure.step('Получение списка заказов: GET /api/v1/orders')
    def get_list_orders():
        return requests.get(urls.BASE_URL + urls.LIST_ORDERS)
