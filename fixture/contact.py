# -*- coding: utf-8 -*-

class ContactHelper:

    def __init__(self, app):
        self.app = app

    # Часто повторяющаяся группа "click() clear() send_keys()" вынесены в отдельный метод setvalue
    def setvalue(self, value, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(value).click()
            wd.find_element_by_name(value).clear()
            wd.find_element_by_name(value).send_keys(text)

    def add(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
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

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # Нажимаем по значку редактирования контакта
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
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
        # Нажимаем кнопку "Update"
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # Выбраем контакт
        wd.find_element_by_name("selected[]").click()
        # Нажимаем по кнопке для удаления
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # Подтверждаем удаление
        wd.switch_to_alert().accept()