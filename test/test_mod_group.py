# -*- coding: utf-8 -*-

from model.group import Group

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    app.group.modify_first_group(Group(name="aaaa_mod"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    app.group.modify_first_group(Group(header="bbbb_mod"))


def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    app.group.modify_first_group(Group(footer="cccc_mod"))