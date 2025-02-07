import allure
from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators
from config import *

class ResetPasswordPage(BasePage):

    @allure.step('Открытие страницы {url}')
    def open_url(self, url):
        self.get_url(url)

    @allure.step('Получение текста заголовка страницы "Сброса пароля"')
    def get_title_page(self):
        return self.get_text_from_element(ResetPasswordPageLocators.PASSWORD_RESET_TITLE)

    @allure.step('Клик на кнопку "Показать/скрыть пароль"')
    def click_to_button_show_hide_password(self):
        self.click_to_element(ResetPasswordPageLocators.SHOW_HIDE_BUTTON)


    @allure.step('Получение атрибута "class" у поля ввода пароля')
    def get_class_password_input(self):
        return self.get_element_attribute(ResetPasswordPageLocators.PASSWORD_INPUT_FIELD, 'class')
