import pytest
from methods.courier_methods import CourierMethods
import allure

class TestCreateCouriers:

    @allure.title('Создание курьера')
    def test_create_couriers(self, courier_methods, login, password, first_name):
        payload = {"login": login, "password": password,"firstName": first_name}
        response = courier_methods.post_courier(payload)
        assert response.status_code == 201 and response.json() == {"ok":True}

    @allure.title('Проверка создания двух одинаковых курьеров')
    def test_create_doblucate_couriers(self, courier_methods, login, password, first_name):
        payload = {"login": login,"password": password,"firstName": first_name }
        # создание нового курьера
        courier_methods.post_courier(payload)
        # создания второго курьера с теми же значениями
        response = courier_methods.post_courier(payload)
        assert response.status_code == 409 and response.json() == {"code": 409,
            "message": "Этот логин уже используется. Попробуйте другой."}


    @allure.title('Проверка создания курьера без логина')
    def test_create_couriers_without_login(self, courier_methods, password, first_name):
        payload = {"password": password, "firstName": first_name}
        response = courier_methods.post_courier(payload)
        assert response.status_code == 400 and response.json() == { "code": 400,
            "message": "Недостаточно данных для создания учетной записи"}
        

    @allure.title('Проверка создания курьера без пароля')
    def test_create_couriers_without_password(self, courier_methods, login, first_name):
        payload = {"login": login, "firstName": first_name}
        response = courier_methods.post_courier(payload)
        assert response.status_code == 400 and response.json() == { "code": 400,
            "message": "Недостаточно данных для создания учетной записи"}
        

    @allure.title('Создание курьера по логину и паролю')
    def test_create_couriers_with_login_and_password(self, courier_methods, login, password):
        payload = {"login": login,"password": password}
        response = courier_methods.post_courier(payload)
        assert response.status_code == 201 and response.json() == {"ok":True}