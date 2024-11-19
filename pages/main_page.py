import allure
from data import *
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Открытие страницы {url}')
    def open_url(self, url):
        self.get_url(url)

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_to_button_personal_page(self):
        self.click_to_element(MainPageLocators.PERSONAL_PAGE_BUTTON)

    @allure.step('Клик на кнопку "Войти в аккаунт"')
    def click_to_button_enter_account(self):
        self.click_to_element(MainPageLocators.ENTER_ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку "Конструктор"')
    def click_to_button_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_to_button_order_feed(self):
        self.click_to_element(MainPageLocators.ORDERS_FEED_BUTTON)

    @allure.step('Получение текста заголовка страницы конструктора')
    def get_title_page(self):
        return self.get_text_from_element(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Клик на ингредиент {ingredient}')
    def click_to_ingredient_with_presence(self, ingredient):
        ingredient_locator = self.format_locator(MainPageLocators.BASE_INGREDIENT_BUTTON, ingredient)
        self.click_to_element_with_presence(ingredient_locator)

    @allure.step('Клик на кнопку-крестик в окне с деталями')
    def click_to_button_window_close(self):
        self.click_to_element(MainPageLocators.WINDOW_CLOSE_BUTTON)

    @allure.step('Получение атрибута "class" у окна с деталями ингредиента {ingredient}')
    def get_class_details_window(self, ingredient):
        ingredient_window_locator = self.format_locator(MainPageLocators.BASE_INGREDIENT_WINDOW, ingredient)
        return self.get_element_attribute(ingredient_window_locator, 'class')

    @allure.step('Получение атрибута "class" у окна с деталями ингредиента {ingredient}')
    def get_class_details_window_with_presence(self, ingredient):
        ingredient_window_locator = self.format_locator(MainPageLocators.BASE_INGREDIENT_WINDOW, ingredient)
        return self.get_element_attribute_with_presence(ingredient_window_locator, 'class')

    @allure.step('Получение атрибута "class" у окна с подтверждением созданного заказа')
    def get_class_order_confirm_window(self):
        return self.get_element_attribute(MainPageLocators.ORDER_CONFIRM_WINDOW, 'class')

    @allure.step('Добавление ингредиента {ingredient} в заказ')
    def add_ingredient(self, ingredient):
        ingredient_locator = self.format_locator(MainPageLocators.BASE_INGREDIENT_BUTTON, ingredient)
        element = self.find_element_with_wait_presence(ingredient_locator)
        target = self.find_element_with_wait_visibility(MainPageLocators.BASKET_CONSTRUCTOR)
#        self.drag_and_drop_ingredient(element, target)
        self.drag_and_drop_with_js(element, target)

    @allure.step('Добавление ингредиентов в заказ')
    def add_ingredients(self):
        for ingredient in INGREDIENTS:
            self.add_ingredient(ingredient)

    @allure.step('Создание заказа')
    def set_order(self):
        self.click_to_button_constructor()
        self.add_ingredients()
        self.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Получение значения каунтера ингредиента {ingredient}')
    def get_counter_value(self, ingredient):
        counter_locator = self.format_locator(MainPageLocators.BASE_COUNTER_INGREDIENT, ingredient)
        return self.get_text_from_element(counter_locator)

    @allure.step('Получение номера нового заказа в окне подтверждения')
    def get_order_number(self):
        return self.get_text_from_element_with_text_presence(MainPageLocators.ORDER_NUMBER_IN_CONFIRM, '1')

    @allure.step('Авторизация в браузере')
    def set_authorization(self, argument):
        self.authorization(argument)
