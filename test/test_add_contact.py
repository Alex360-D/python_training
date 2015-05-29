# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.contact.add(Contact(firstname="Alexander", middlename="Alex", lastname="Paderin", nickname="Alex360",
                                     title="Alex-title", company="Alex Company", address="Russia, Moscow City, 11",
                                     home="+7(495)111-11-11", mobile="+7(495)222-22-22", work="+7(495)333-33-33", fax="+7(495)444-44-44",
                                     email="alex@alex.ru", email2="alex2@alex.ru", email3="alex3@alex.ru", homepage="http://alexhomepage.ru",
                                     byear="1984", address2="Russia, Moscow City, 15", phone2="5555", notes="simple notes"))