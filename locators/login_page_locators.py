from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Ссылка для восстановления пароля
    PASSWORD_RECOVERY_LINK = By.XPATH, './/a[text()="Восстановить пароль"]'
    # Заголовок страницы авторизации
    LOGIN_PAGE_TITLE = By.XPATH, './/div[@class="Auth_login__3hAey"]/h2'
    # Форма ввода email пользователя
    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/following-sibling::input'
    # Форма ввода пароля пользователя
    PASSWORD_INPUT = By.XPATH, './/label[text()="Пароль"]/following-sibling::input'
    # Кнопка «Войти»
    ENTER_BUTTON = By.XPATH, './/button[text()="Войти"]'
