# -*- coding: utf-8 -*-

from model.contact import Contact
from model.group import Group

import random

def test_add_contact_in_group(app, orm):
    # Проверяем что есть контакты, и если нет, то добавляем один контакт
    if len(orm.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="test_contact"))
    # Считываем из БД список контактов
    list_contacts = orm.get_contact_list()
    # Выбираем один случайный контакт
    contact = random.choice(list_contacts)
    # Ищем группы, в которых этого контакта нет; и если таких групп вообще нет, то создаём новую группу
    if len(orm.get_groups_without_contact(Contact(id=contact.id))) == 0:
        app.group.create(Group(name="test_group"))
    groups = orm.get_groups_without_contact(Contact(id=contact.id))
    # Выбираем одну случайную группу из списка
    group = random.choice(groups)
    # Добавляем контакт в группу
    app.contact.move_contact_in_group(contact.id, group.name)
    # Проверяем, что контакт находится в указанной группе
    contact_in_group = orm.get_contacts_in_group(sorted(orm.get_group_list_by_name(Group(name=group.name)), key=Group.id_or_max)[0])
    assert contact_in_group[0] == contact