from selenium.webdriver.common.by import By


class MainPageLocators:
    # Заголовок страницы конструктора
    CONSTRUCTOR_TITLE = By.XPATH, './/h1[contains(@class, "text_type_main-large")]'
    # Кнопка "Личный кабинет" на главной странице
    PERSONAL_PAGE_BUTTON = By.XPATH, './/p[text()="Личный Кабинет"]'
    # Кнопка "Войти в аккаунт" на главной странице
    ENTER_ACCOUNT_BUTTON = By.XPATH, './/button[text()="Войти в аккаунт"]'
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = By.XPATH, './/p[text()="Конструктор"]'
    # Кнопка "Лента Заказов"
    ORDERS_FEED_BUTTON = By.XPATH, './/p[text()="Лента Заказов"]'
    # Кнопка "Оформить заказ"
    CREATE_ORDER_BUTTON = By.XPATH, './/button[text()="Оформить заказ"]'
    # Кнопка закрытия окна с деталями ингредиента
    WINDOW_CLOSE_BUTTON = By.XPATH, './/section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/div/button'
    # Общий локатор ингредиента
    BASE_INGREDIENT_BUTTON = './/p[starts-with(@class, "BurgerIngredient") and contains(text(), "{}")]'
    # Общий локатор окна с деталями ингредиента
    BASE_INGREDIENT_WINDOW = './/p[starts-with(@class, "text") and contains(text(), "{}")]/' \
                             'parent::div/parent::div/parent::section'
    # Общий локатор каунтера ингредиента
    BASE_COUNTER_INGREDIENT = './/img[@alt="{}"]/preceding-sibling::div/p'
    # Локатор конструктора бургера
    BASKET_CONSTRUCTOR = By.XPATH, './/section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]'
    # Окно подтверждения созданного заказа
    ORDER_CONFIRM_WINDOW = By.XPATH, './/p[text()="идентификатор заказа"]/parent::div/parent::div/parent::section'
    # Номер заказа в окне подтверждения
    ORDER_NUMBER_IN_CONFIRM = By.XPATH, './/h2[contains(@class, "Modal_modal__title__2L34m")]'
