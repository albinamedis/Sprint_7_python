BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
ORDER_URL = 'orders/'

data_order = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha"
}

message_code_400 = 'Недостаточно данных для создания учетной записи'
message_code_409 = 'Этот логин уже используется. Попробуйте другой.'
message_code_404 = 'Учетная запись не найдена'
message_code_400_login = 'Недостаточно данных для входа'