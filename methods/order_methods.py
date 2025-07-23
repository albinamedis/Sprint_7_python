import requests
import allure
from data import BASE_URL

class OrderMethods:

    def __init__(self, url=None):
        self.url = url

    @allure.step("Создание заказа")
    def post_orders(self, params):
        response = requests.post(f"{BASE_URL}orders", data = params)
        return response
    
    @allure.step("Получение списка заказов")
    def get_orders(self):
        response = requests.get(f"{BASE_URL}orders")
        return response