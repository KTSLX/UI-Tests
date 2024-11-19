from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    # Ссылка для перехода в раздел 'История заказов'
    ORDER_HISTORY_LINK = By.LINK_TEXT, 'История заказов'
    # Локатор номера заказа в истории заказов
    ORDER_NUMBER = By.XPATH, './/ul[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]/li[last()]/a/div[@class="OrderHistory_textBox__3lgbs mb-6"]/' \
                             'p[@class="text text_type_digits-default"]'
