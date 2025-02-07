from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    # Заголовок страницы восстановления пароля
    PASSWORD_RECOVERY_TITLE = By.XPATH, './/div[@class="Auth_login__3hAey"]/h2'
    # Кнопка "Восстановить"
    RECOVERY_BUTTON = By.XPATH, './/button[text()="Восстановить"]'
    # Форма ввода email пользователя
    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/following-sibling::input'
