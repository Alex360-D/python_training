# -*- coding: utf-8 -*-
# Вариант №2: оптимизированная версия test_add_contact.py
# Из метода "def add_contact" вынесена группа "click() clear() send_keys()" в отдельный метод "def setvalue"

from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    # Часто повторяющаяся группа "click() clear() send_keys()" вынесены в отдельный метод setvalue
    def setvalue(self, value, contact):
        self.wd.find_element_by_name(value).click()
        self.wd.find_element_by_name(value).clear()
        self.wd.find_element_by_name(value).send_keys(contact)

    def add_contact(self, wd, contact):
        # Выбираем "Add new"
        wd.find_element_by_link_text("add new").click()
        # Заполняем поля
        self.setvalue("firstname", contact.firstname)
        self.setvalue("middlename", contact.middlename)
        self.setvalue("lastname", contact.lastname)
        self.setvalue("nickname", contact.nickname)
        self.setvalue("title", contact.title)
        self.setvalue("company", contact.company)
        self.setvalue("address", contact.address)
        self.setvalue("home", contact.home)
        self.setvalue("mobile", contact.mobile)
        self.setvalue("work", contact.work)
        self.setvalue("fax", contact.fax)
        self.setvalue("email", contact.email)
        self.setvalue("email2", contact.email2)
        self.setvalue("email3", contact.email3)
        self.setvalue("homepage", contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[12]").click()
        self.setvalue("byear", contact.byear)
        self.setvalue("address2", contact.address2)
        self.setvalue("phone2", contact.phone2)
        self.setvalue("notes", contact.notes)
        # Нажимаем кнопку "Enter" (Подтвердить введённые данные)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_contact(wd, Contact(firstname="Alexander", middlename="Alex", lastname="Paderin", nickname="Alex360",
                                     title="Alex-title", company="Alex Company", address="Russia, Moscow City, 11",
                                     home="+7(495)111-11-11", mobile="+7(495)222-22-22", work="+7(495)333-33-33", fax="+7(495)444-44-44",
                                     email="alex@alex.ru", email2="alex2@alex.ru", email3="alex3@alex.ru", homepage="http://alexhomepage.ru",
                                     byear="1984", address2="Russia, Moscow City, 15", phone2="5555", notes="simple notes"))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()