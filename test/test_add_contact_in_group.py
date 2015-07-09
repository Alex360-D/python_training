# -*- coding: utf-8 -*-

from model.contact import Contact
from model.group import Group
import random

def test_add_contact_in_group(app, orm):
    # Проверяем что есть контакты, и если нет, то добавляем один контакт
    if len(orm.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="test_contact"))
    # Проверяем что есть группы, и если нет, то добавляем одну группу
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test_group"))
    # Считываем из БД список контактов и групп
    list_contacts = orm.get_contact_list()
    list_groups = orm.get_group_list()
    # Выбираем из этих списков один случайный контакт и одну случайную группу
    # Контакт не должен находится в выбранной группе
    pass
    contact = random.choice(list_contacts)
    group = random.choice(list_groups)
    # Добавляем контакт в группу
    app.contact.move_contact_in_group(contact.id, group.name)
    # Проверяем, что контакт находится в указанной группе
    pass

    '''
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    '''