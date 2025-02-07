import requests
import allure
import random
import string
from data import *


@allure.step('Генерация строки с задаваемой длиной, состоящей из {length} букв нижнего регистра')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерация данных из email, пароля и имени для нового пользователя')
def generate_random_payload():
    login = generate_random_string(6)
    password = generate_random_string(6)
    name = generate_random_string(6)
    payload = {
        'email': login + '@yandex.ru',
        'password': password,
        'name': name
    }
    return payload


@allure.step('Регистрация нового пользователя и получение списка из его email, пароля и имени')
def register_new_user_and_return_email_password():
    login_data = []
    payload = generate_random_payload()
    response = requests.post(API_REGISTER_URL, data=payload)
    if response.status_code == 200:
        login_data.append(payload['email'])
        login_data.append(payload['password'])
        login_data.append(payload['name'])
    return login_data
