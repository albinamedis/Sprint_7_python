import pytest
from methods.courier_methods import CourierMethods
import allure
from data import message_code_404, message_code_400_login

class TestAuthCouriers:

    @allure.title('Авторизация курьера в системе')
    def test_login_couriers(self, courier_methods, login, password):
        payload = {"login": login, "password": password}
        # регистрируем курьера
        courier_methods.post_courier(payload)
        # авторизуемся
        response = courier_methods.post_courier_login(payload)
        assert response.status_code == 200 and response.json()['id'] is not None

    @allure.title('Авторизация курьера в системе без пароля')
    def test_auth_couriers_without_password(self, courier_methods, login):
        payload = {"login": login}
        response = courier_methods.post_courier_login(payload)
        assert response.status_code == 504

    @allure.title('Авторизация курьера в системе без логина')
    def test_auth_couriers_without_login(self, courier_methods, password):
        payload = {"password": password}
        response = courier_methods.post_courier_login(payload)
        assert response.status_code == 400 and response.json()['message'] == message_code_400_login
        
    @allure.title('Авторизация не существующего курьера в системе')
    def test_login_couriers_not_found(self, courier_methods, login, password):
        payload = {"login": login, "password": password}
        response = courier_methods.post_courier_login(payload)
        assert response.status_code == 404 and response.json()['message'] == message_code_404