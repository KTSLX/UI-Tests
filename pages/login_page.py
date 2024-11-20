import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step('Открытие страницы {url}')
    def open_url(self, url):
        self.get_url(url)

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_to_button_recovery_password(self):
        self.click_to_element(LoginPageLocators.PASSWORD_RECOVERY_LINK)

    @allure.step('Клик на кнопку "Войти"')
    def click_to_button_enter(self):
        self.click_to_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Получение текста заголовка страницы авторизации')
    def get_title_page(self):
        return self.get_text_from_element(LoginPageLocators.LOGIN_PAGE_TITLE)

    @allure.step('Ввод почты {email} в поле "Email"')
    def set_email(self, email):
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Ввод пароля {password} в поле "Пароль"')
    def set_password(self, password):
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT, password)