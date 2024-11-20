import os
import sys
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import API_LOGIN_URL, API_USER_URL
from helpers import register_new_user_and_return_email_password

# Добавляем корневую директорию в PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')  # Работает для Chrome
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        # Устанавливаем разрешение окна для Firefox
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()


@pytest.fixture
def register_user():
    """
    Регистрирует нового пользователя, возвращает данные пользователя и токен,
    удаляет пользователя после завершения теста.
    """
    user = register_new_user_and_return_email_password()
    payload = {
        'email': user[0],
        'password': user[1],
        'name': user[2]
    }
    login_response = requests.post(API_LOGIN_URL, data=payload)
    token = login_response.json().get('accessToken')
    if not token:
        raise RuntimeError("Failed to fetch access token during user registration.")

    yield {
        'email': user[0],
        'password': user[1],
        'name': user[2],
        'token': token
    }

    # Удаляем пользователя после завершения теста
    requests.delete(API_USER_URL, headers={'Authorization': token})
