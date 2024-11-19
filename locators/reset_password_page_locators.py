from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    # Заголовок страницы сброса пароля
    PASSWORD_RESET_TITLE = By.XPATH, './/div[@class="Auth_login__3hAey"]/h2'
    # Форма ввода пароля пользователя
    PASSWORD_INPUT = By.XPATH, './/input[@name="Введите новый пароль"]'
    # Кнопка "Показать/скрыть пароль"
    SHOW_HIDE_BUTTON = By.XPATH, './/div[@class="input__icon input__icon-action"]'
    # Поле ввода пароля пользователя
    PASSWORD_INPUT_FIELD = By.XPATH, './/label[text()="Пароль"]/parent::div'
