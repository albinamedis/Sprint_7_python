import requests
import allure
import random
import string
from data import BASE_URL

class CourierMethods:

    @allure.step("Создание нового курьера")
    def post_courier(self, params):
        response = requests.post(f"{BASE_URL}courier", data = params)
        return response

    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step("Логин курьера в системе")
    def post_courier_login(self, params):
        response = requests.post(f"{BASE_URL}courier/login", data = params)
        return response