# -*- coding: utf-8 -*-

from model.contact import Contact
from model.group import Group
# from .test_add_contact_in_group import test_add_contact_in_group
import random

def test_del_contact_from_group(app, orm):
    # Проверяем, что есть группы с контактами, если нет, то добавляем группу и контакт в группу
    # if (len(orm.get_group_list()) == 0) and (len(orm.get_contact_list()) == 0):
    #     test_add_contact_in_group(app, orm)

    list_groups = orm.get_group_list()
    group = random.choice(list_groups)
    if len(orm.get_contacts_in_group(group)) == 0:
        app.group.create(Group(name="test_group"))
    # Считываем из БД список групп, у которых есть контакты
    # Выбираем одну случайную группу
    # Выбираем один случайный контакт из этой группы
    # Удаляем контакт из группы
    # Проверяем, что контакта в группе нет
    pass