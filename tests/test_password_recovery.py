import pytest
import allure
from data import *
from helpers import *
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.login_page import LoginPage
from conftest import driver


class TestPasswordRecovery:

    @classmethod
    def setup_class(cls):
        cls.user = register_new_user_and_return_email_password()
        cls.payload = {
            'email': cls.user[0],
            'password': cls.user[1],
            'name': cls.user[2]
        }
        login_response = requests.post(API_LOGIN_URL, data=cls.payload)
        cls.user_token = login_response.json()['accessToken']

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('Выполняется нажатие на кнопку "Восстановить пароль" и проверяется заголовок страницы.')
    def test_enter_page_forgot_password(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_URL)
        login_page.click_to_button_recovery_password()
        assert forgot_password_page.get_title_page() == EXPECTED_RECOVERY_PASSWORD_TITLE

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    @allure.description('Выполняется ввода почты, клик по кнопке "Восстановить" и проверяется заголовок страницы.')
    def test_enter_page_reset_password(self, driver):
        reset_password_page = ResetPasswordPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_url(FORGOT_PASSWORD_URL)
        forgot_password_page.set_email(self.payload['email'])
        forgot_password_page.click_to_button_recovery()
        assert reset_password_page.get_title_page() == EXPECTED_RECOVERY_PASSWORD_TITLE

    @allure.title('Проверка клика по кнопке "Показать/скрыть пароль"')
    @allure.description('Выполняется проверка активации и подсвечивания поля ввода пароля при нажатии на кнопку.')
    def test_activation_field_email_after_click(self, driver):
        reset_password_page = ResetPasswordPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_url(FORGOT_PASSWORD_URL)
        forgot_password_page.set_email(self.payload['email'])
        forgot_password_page.click_to_button_recovery()
        reset_password_page.click_to_button_show_hide_password()
        assert EXPECTED_INPUT_CLASS in reset_password_page.get_class_password_input()

    @classmethod
    def teardown_class(cls):
        requests.delete(API_USER_URL, headers={'Authorization': cls.user_token})