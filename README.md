##  Task 3: UI tests

### Automated tests for Stellar Burgers ordering system

### Technology stack:

* Pytest
* Selenium
* Requests
* Allure

### Implemented Scenarios:

UI tests: `Main ordering scenario`, `Orders Feed`, `Password recovery`, `My Profile`.

### Project structure

- `Diploma_3` - project, containing tests and support modules.
- `tests` - a folder, containing tests, divided by classes: `test_main_functional.py`, `test_orders_feed.py`, `test_password_recovery.py`, `test_personal_page.py`.

### Launching the tests:

**Installing requirements**

> `$ pip install -r requirements.txt`

**Launching the tests from `Diploma_3` directory and generation of Allure report summary**

> `pytest tests\ --alluredir=allure_results`
> `allure serve allure_results`
