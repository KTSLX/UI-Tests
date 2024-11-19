##  Дипломный проект. Задание 3: UI тесты

### Автотесты для проверки программы заказа бургеров в Stellar Burgers

### Использованный стек технологий

* Pytest
* Selenium
* Requests
* Allure

### Реализованные сценарии

Созданы UI тесты по тематике: `Проверка основного функционала`, `Раздел «Лента заказов»`, `Восстановление пароля`
, `Личный кабинет `.

### Структура проекта

- `Diplom_3` - проект, содержащий тесты и вспомогательные папки.
- `tests` - пакет, содержащий тесты, разделенные по классам: `test_main_functional.py`, `test_orders_feed.py`
  , `test_password_recovery.py`, `test_personal_page.py`.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов из корня проекта `Diplom_3` и создание HTML-отчета в Allure**

> `pytest tests\ --alluredir=allure_results`
> `allure serve allure_results`
