import pytest
import allure
from data import *
from helpers import *
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from pages.profile_page import ProfilePage
from pages.orders_history_page import OrderHistoryPage
from conftest import driver


class TestOrdersFeed:

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

    @allure.title('Проверка открытия всплывающего окна с деталями по клику на заказ в ленте заказов')
    @allure.description('Выполняется клик на заказ и проверяется открытие окна с деталями.')
    def test_open_order_details_window(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open_url(ORDERS_FEED_URL)
        orders_feed_page.click_to_order()
        assert EXPECTED_OPEN_WINDOW_CLASS in orders_feed_page.get_class_order_details_window()

    @allure.title('Проверка отображения заказов пользователя из раздела "История заказов" на странице "Лента заказов"')
    @allure.description('Оформляется заказ и проверяется отображение его номера в истории в профиле и ленте заказов.')
    def test_display_new_order_in_orders_feed(self, driver):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        order_history_page = OrderHistoryPage(driver)
        orders_feed_page = OrdersFeedPage(driver)
        main_page.open_url(MAIN_URL)
        main_page.set_authorization(self.user_token)
        main_page.click_to_button_enter_account()
        main_page.set_order()
        main_page.click_to_button_window_close()
        main_page.click_to_button_personal_page()
        profile_page.click_to_button_order_history()
        order_number_in_history = order_history_page.get_order_number()
        main_page.click_to_button_order_feed()
        assert orders_feed_page.get_order_number_in_feed() == order_number_in_history

    @allure.title('Проверка увеличения счётчика "Выполнено за все время" и "Выполнено за сегодня" при создании заказа')
    @allure.description('Выполняется оформление заказа и проверяется увеличение счётчика в ленте заказов.')
    @pytest.mark.parametrize('counter_name', COUNTER_NAME)
    def test_orders_counter(self, driver, counter_name):
        main_page = MainPage(driver)
        orders_feed_page = OrdersFeedPage(driver)
        main_page.open_url(MAIN_URL)
        main_page.set_authorization(self.user_token)
        main_page.click_to_button_enter_account()
        main_page.click_to_button_order_feed()
        current_counter = int(orders_feed_page.get_counter_value(counter_name))
        main_page.set_order()
        main_page.click_to_button_window_close()
        main_page.click_to_button_order_feed()
        assert int(orders_feed_page.get_counter_value(counter_name)) == current_counter + 1

    @allure.title('Проверка появления номера нового заказа в разделе "В работе" в ленте заказов')
    @allure.description('Выполняется оформление заказа и проверяется появление его номера в разделе "В работе".')
    def test_show_order_number_in_work(self, driver):
        main_page = MainPage(driver)
        orders_feed_page = OrdersFeedPage(driver)
        main_page.open_url(MAIN_URL)
        main_page.set_authorization(self.user_token)
        main_page.click_to_button_enter_account()
        main_page.set_order()
        order_number_in_confirm = main_page.get_order_number()
        main_page.click_to_button_window_close()
        main_page.click_to_button_order_feed()
        order_number_in_work = orders_feed_page.get_order_number_in_work()
        assert order_number_in_confirm in order_number_in_work

    @classmethod
    def teardown_class(cls):
        requests.delete(API_USER_URL, headers={'Authorization': cls.user_token})
