# -*- coding: utf-8 -*-

from model.contact import Contact

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
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # Нажимаем по значку редактирования контакта
        wd.find_elements_by_css_selector("img[alt=\"Edit\"]")[index].click()
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
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # Выбраем контакт
        wd.find_elements_by_name("selected[]")[index].click()
        # Нажимаем по кнопке для удаления
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # Подтверждаем удаление
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_element_by_xpath("td[2]").text
                firstname = element.find_element_by_xpath("td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname = lastname, firstname = firstname, id = id))
        return list(self.contact_cache)