import pytest
from methods.order_methods import OrderMethods
import allure
import json
from data import data_order

class TestCreateOrder:

    @allure.title('Создание заказа')
    @pytest.mark.parametrize('color', [["BLACK", "GREY"], [],["BLACK"], ["GRAY"]])
    def test_create_order(self, order_methods, color):
        data_order['color'] = color
        json_string = json.dumps(data_order)
        response = order_methods.post_orders(json_string)
        assert response.status_code == 201 and response.json()['track'] is not None

    @allure.title('Поверка получения списка заказов')
    def test_get_order(self, order_methods):
        response = order_methods.get_orders()
        assert response.status_code == 200 and response.json()['orders'][0] is not None