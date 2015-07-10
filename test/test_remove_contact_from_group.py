# -*- coding: utf-8 -*-

from model.contact import Contact
from model.group import Group
import random

def test_remove_contact_from_group(app, orm):
    # Проверяем, что есть группы
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test_group"))
    # Загружаем из БД список групп
    list_groups = orm.get_group_list()
    # Выбираем одну случайную группу
    group = random.choice(list_groups)
    # Проверяем группу на наличие у неё контактов
    a = len(orm.get_contacts_in_group(group))
    if len(orm.get_contacts_in_group(group)) == 0:
        # Добавляем контакт в группу, но предварительно проверяем, есть ли вообще контакты
        # Если нет контактов, то создаем один контакт
        if len(orm.get_contact_list()) == 0:
            app.contact.add(Contact(firstname="test_contact"))
        # Выбираем один случайный контакт
        list_contacts = orm.get_contact_list()
        contact = random.choice(list_contacts)
        # Добавляем контакт в группу
        app.contact.move_contact_in_group(contact.id, group.name)
    # Считываем список контактов, присутствующие в этой группе
    list_contacts = orm.get_contacts_in_group(group)
    # Выбираем один случайный контакт
    contact = random.choice(list_contacts)
    # Удаляем контакт из группы
    app.contact.remove_contact_from_group(contact.id, group.name)
    # Проверяем, что контакта в группе нет
    contact_in_group = orm.get_contacts_in_group(sorted(orm.get_group_list_by_name(Group(name=group.name)), key=Group.id_or_max)[0])
    assert contact not in contact_in_group