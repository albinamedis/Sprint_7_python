from data import BASE_URL, ORDER_URL
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods
import pytest

@pytest.fixture
def courier_methods():
    return CourierMethods()

@pytest.fixture
def order_methods():
    return OrderMethods()

@pytest.fixture
def login(courier_methods):
    login = courier_methods.generate_random_string(10)
    return login

@pytest.fixture
def password(courier_methods):
    password = courier_methods.generate_random_string(10)
    return password

@pytest.fixture
def first_name(courier_methods):
    first_name = courier_methods.generate_random_string(10)
    return first_name