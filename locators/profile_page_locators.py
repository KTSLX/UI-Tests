from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Ссылка для перехода в раздел 'История заказов'
    PROFILE_LINK = By.LINK_TEXT, 'Профиль'
    # Ссылка для перехода в раздел 'История заказов'
    ORDER_HISTORY_LINK = By.LINK_TEXT, 'История заказов'
    # Кнопка «Выход»
    EXIT_BUTTON = By.XPATH, ".//button[text()='Выход']"
