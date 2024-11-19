import allure
from pages.base_page import BasePage
from locators.orders_history_page_locators import OrderHistoryPageLocators


class OrderHistoryPage(BasePage):

    @allure.step('Получение атрибута "class" у элемента')
    def get_element_attribute_class(self):
        return self.get_element_attribute(OrderHistoryPageLocators.ORDER_HISTORY_LINK, 'class')

    @allure.step('Получение номера заказа пользователя в истории заказов в личном кабинете')
    def get_order_number(self):
        return self.get_text_from_element(OrderHistoryPageLocators.ORDER_NUMBER)