import os
import sys

# Добавляем корневую директорию в PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from data import *


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
