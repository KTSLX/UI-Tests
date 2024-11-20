import pytest
import allure
from data import *
from helpers import *
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.login_page import LoginPage
from conftest import driver, register_user


class TestPasswordRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('Выполняется нажатие на кнопку "Восстановить пароль" и проверяется заголовок страницы.')
    def test_enter_page_forgot_password(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_URL)
        login_page.click_to_button_recovery_password()
        assert forgot_password_page.get_title_page() == EXPECTED_RECOVERY_PASSWORD_TITLE

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    @allure.description('Выполняется ввод почты, клик по кнопке "Восстановить" и проверяется заголовок страницы.')
    def test_enter_page_reset_password(self, driver, register_user):
        reset_password_page = ResetPasswordPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        forgot_password_page.open_url(FORGOT_PASSWORD_URL)
        forgot_password_page.set_email(register_user['email'])
        forgot_password_page.click_to_button_recovery()
        assert reset_password_page.get_title_page() == EXPECTED_RECOVERY_PASSWORD_TITLE

    @allure.title('Проверка клика по кнопке "Показать/скрыть пароль"')
    @allure.description('Выполняется проверка активации и подсвечивания поля ввода пароля при нажатии на кнопку.')
    def test_activation_field_email_after_click(self, driver, register_user):
        reset_password_page = ResetPasswordPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        forgot_password_page.open_url(FORGOT_PASSWORD_URL)
        forgot_password_page.set_email(register_user['email'])
        forgot_password_page.click_to_button_recovery()
        reset_password_page.click_to_button_show_hide_password()
        assert EXPECTED_INPUT_CLASS in reset_password_page.get_class_password_input()
