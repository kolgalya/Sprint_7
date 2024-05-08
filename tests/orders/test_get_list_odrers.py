from scooter_api import ScooterApi
import allure

class TestListOrders:
    @allure.description('Получение списка заказов')
    def test_can_create_order(self):
        list_order = ScooterApi.get_list_orders()
        assert list_order.status_code == 200 and list_order.json()["orders"] != []
