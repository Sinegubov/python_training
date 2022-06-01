# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    group_static = Group(name="New group")
    if len(db.get_group_list()) == 0:
        app.group.create(group_static)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max()) == sorted(app.group.get_group_list(), key=Group.id_or_max())



# def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    assert len(old_groups) == app.group.count()


# def test_modify_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(footer="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer="New footer"))
#    assert len(old_groups) == app.group.count()
