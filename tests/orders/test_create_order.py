import pytest
from scooter_api import ScooterApi
from data import TestDataCreateOrder as TDCO
import allure

class TestCreateOrder:
    @allure.description('Можно создать заказ')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], ''])
    def test_can_create_order(self, color):
        body = TDCO.create_order_body(color)
        order = ScooterApi.create_order(body)
        assert order.status_code == 201 and 'track' in order.json()
