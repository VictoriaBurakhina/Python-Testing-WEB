import time

import pytest
from testpage import OperationHelper
username = "GB98057365"
password = "c2d0106e9e"

def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("GB98057365")
    test_page1.enter_pswd("c2d0106e9e")
    test_page1.click_button()
    time.sleep(3)
#авторизация
    test_page1.click_contact()
    time.sleep(3)
    #Заполнение полей
    test_page1.enter_cont_name("Victoria")
    test_page1.enter_cont_email("list@yandex.ru")
    test_page1.enter_cont_text("Some text")
    time.sleep(1)
    #нажатие кнопки
    test_page1.click_button()
    time.sleep(1)
#проверка текста всплывающего окна
    assert test_page1.get_alert_text() == "Form successfully submitted"
