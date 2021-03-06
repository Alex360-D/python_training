# -*- coding: utf-8 -*-

from model.group import Group
from random import randrange
import pytest

def test_modify_some_group_name(app, db, check_ui):
    with pytest.allure.step('Given a group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test_group"))
        old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="aaaa_mod")
    group.id = old_groups[index].id
    with pytest.allure.step('When I modify the group with id=%s in the list' % group.id):
        app.group.modify_group_by_id(group.id, group)
    with pytest.allure.step('Then the new group list is equal to the old list with the modified group'):
        new_groups = db.get_group_list()
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        with pytest.allure.step('Also check UI'):
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)