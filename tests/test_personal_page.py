import pytest
import allure
from data import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.orders_history_page import OrderHistoryPage
from conftest import driver, register_user


class TestPersonalPage:

    @allure.title('Проверка перехода в личный кабинет по клику на кнопку "Личный кабинет"')
    @allure.description('Выполняется авторизация по клику на кнопку "Личный кабинет" и проверка активации страницы.')
    def test_enter_in_personal_page(self, driver, register_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_url(MAIN_URL)
        main_page.click_to_button_personal_page()
        login_page.set_email(register_user['email'])
        login_page.set_password(register_user['password'])
        login_page.click_to_button_enter()
        main_page.click_to_button_personal_page()
        assert EXPECTED_PROFILE_CLASS in profile_page.get_element_attribute_class()

    @allure.title('Проверка перехода в раздел "История заказов"')
    @allure.description('Выполняется авторизация, переход в раздел "История заказов" и проверяется активация страницы.')
    def test_enter_in_order_history_page(self, driver, register_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        order_history_page = OrderHistoryPage(driver)

        login_page.open_url(LOGIN_URL)
        login_page.set_email(register_user['email'])
        login_page.set_password(register_user['password'])
        login_page.click_to_button_enter()
        main_page.click_to_button_personal_page()
        profile_page.click_to_button_order_history()
        assert EXPECTED_HISTORY_CLASS in order_history_page.get_element_attribute_class()

    @allure.title('Проверка выхода из личного кабинета')
    @allure.description('Выполняется авторизация, нажатие на кнопку "Выход" и проверка заголовка страницы после выхода.')
    def test_exit_from_personal_page(self, driver, register_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        login_page.open_url(LOGIN_URL)
        login_page.set_email(register_user['email'])
        login_page.set_password(register_user['password'])
        login_page.click_to_button_enter()
        main_page.click_to_button_personal_page()
        profile_page.click_to_button_exit()
        assert login_page.get_title_page() == EXPECTED_LOGIN_TITLE
