from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:
    # Заголовок страницы ленты заказов
    ORDERS_FEED_TITLE = By.XPATH, './/h1[contains(@class, "text_type_main-large")]'
    # Название первого бургера в ленте
    BURGER_NAME = By.XPATH, './/h2[@class="text text_type_main-medium mb-2"]'
    # Номер первого заказа в ленте заказов
    ORDER_NUMBER_IN_FEED = By.XPATH, './/div[@class="OrderHistory_textBox__3lgbs mb-6"]/' \
                                     'p[@class="text text_type_digits-default"]'
    # Окно деталей заказа
    ORDER_DETAILS_WINDOW = By.XPATH, './/p[text()="Cостав"]/parent::div/parent::div/parent::section'
    # Общий локатор счётчика в ленте заказов
    BASE_ORDERS_COUNTER = './/p[text()="{}"]/following-sibling::p'
    # Номер заказа в разделе "В работе"
    ORDER_NUMBER_IN_WORK = By.XPATH, './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/' \
                                     'li[@class="text text_type_digits-default mb-2"]'
