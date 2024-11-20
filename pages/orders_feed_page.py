import allure
from pages.base_page import BasePage
from locators.orders_feed_page_locators import OrdersFeedPageLocators
import time
from config import *

class OrdersFeedPage(BasePage):

    @allure.step('Открытие страницы {url}')
    def open_url(self, url):
        self.get_url(url)

    @allure.step('Получение текста заголовка страницы ленты заказов')
    def get_title_page(self):
        return self.get_text_from_element(OrdersFeedPageLocators.ORDERS_FEED_TITLE)

    @allure.step('Клик на заказ')
    def click_to_order(self):
        self.click_to_element(OrdersFeedPageLocators.BURGER_NAME)

    @allure.step('Получение атрибута "class" у окна с деталями заказа')
    def get_class_order_details_window(self):
        return self.get_element_attribute(OrdersFeedPageLocators.ORDER_DETAILS_WINDOW, 'class')

    @allure.step('Получение номера заказа пользователя в ленте заказов')
    def get_order_number_in_feed(self):
        time.sleep(1)
        return self.get_text_from_element(OrdersFeedPageLocators.ORDER_NUMBER_IN_FEED)

    @allure.step('Получение номера заказа в разделе "В работе"')
    def get_order_number_in_work(self):
        return self.get_text_from_element_with_presence(OrdersFeedPageLocators.ORDER_NUMBER_IN_WORK)

    @allure.step('Получение значения счётчика {counter_name}')
    def get_counter_value(self, counter_name):
        counter_locator = self.format_locator(OrdersFeedPageLocators.BASE_ORDERS_COUNTER, counter_name)
        return self.get_text_from_element(counter_locator)