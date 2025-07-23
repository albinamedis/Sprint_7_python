import pytest
from methods.courier_methods import CourierMethods
import allure
from data import message_code_400, message_code_409

class TestCreateCouriers:

    @allure.title('Создание курьера')
    def test_create_couriers(self, courier_methods, login, password, first_name, delete_courier):
        payload = {"login": login, "password": password,"firstName": first_name}
        response = courier_methods.post_courier(payload)
        assert response.status_code == 201 and response.json() == {"ok":True}
        delete_courier(login, password)
        
    @allure.title('Проверка создания двух одинаковых курьеров')
    def test_create_doblucate_couriers(self, courier_methods, login, password, first_name, delete_courier):
        payload = {"login": login,"password": password,"firstName": first_name }
        # создание нового курьера
        courier_methods.post_courier(payload)
        # создания второго курьера с теми же значениями
        response = courier_methods.post_courier(payload)
        assert response.status_code == 409 and response.json()["message"] == message_code_409
        delete_courier(login, password)


    @allure.title('Проверка создания курьера без пароля/логина')
    @pytest.mark.parametrize('missing_field', ["login", "password"])
    def test_create_couriers_without_login_or_password(self, courier_methods, login, password, first_name, missing_field):
            payload = {"login": login, "password": password, "firstName": first_name}
            payload.pop(missing_field)
            response = courier_methods.post_courier(payload)
            assert response.status_code == 400 and response.json()["message"] == message_code_400


    @allure.title('Создание курьера по логину и паролю')
    def test_create_couriers_with_login_and_password(self, courier_methods, login, password, delete_courier):
        payload = {"login": login,"password": password}
        response = courier_methods.post_courier(payload)
        assert response.status_code == 201 and response.json() == {"ok":True}
        delete_courier(login, password)