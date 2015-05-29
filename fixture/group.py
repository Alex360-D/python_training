# -*- coding: utf-8 -*-

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def setvalue(self, value, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(value).click()
            wd.find_element_by_name(value).clear()
            wd.find_element_by_name(value).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.setvalue("group_name", group.name)
        self.setvalue("group_header", group.header)
        self.setvalue("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # Выбираем "New group"
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Нажимаем "Submit"
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # Нажимаем "Edit"
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # Нажимаем "Update"
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # Нажимаем по кнопке для удаления
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
