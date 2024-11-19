import allure
from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators

class ForgotPasswordPage(BasePage):

    @allure.step('Открытие страницы {url}')
    def open_url(self, url):
        self.get_url(url)

    @allure.step('Получение текста заголовка страницы "Восстановление пароля"')
    def get_title_page(self):
        return self.get_text_from_element(ForgotPasswordPageLocators.PASSWORD_RECOVERY_TITLE)

    @allure.step('Клик на кнопку "Восстановить"')
    def click_to_button_recovery(self):
        self.click_to_element(ForgotPasswordPageLocators.RECOVERY_BUTTON)

    @allure.step('Ввод почты {email} в поле "Email"')
    def set_email(self, email):
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, email)