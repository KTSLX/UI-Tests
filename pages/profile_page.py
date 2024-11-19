import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step('Клик на кнопку "История заказов"')
    def click_to_button_order_history(self):
        self.click_to_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('Клик на кнопку "Выход"')
    def click_to_button_exit(self):
        self.click_to_element(ProfilePageLocators.EXIT_BUTTON)

    @allure.step('Получение атрибута "class" у элемента')
    def get_element_attribute_class(self):
        return self.get_element_attribute(ProfilePageLocators.PROFILE_LINK, 'class')