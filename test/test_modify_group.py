# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    group_s = Group(name="New group")
    if len(db.get_group_list()) == 0:
        app.group.create(group_s)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, group_s)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == \
               sorted(app.group.get_contact_list(), key=Group.id_or_max)


def test_modify_group_header(app, db, check_ui):
    group_s = Group(header="test")
    if len(db.get_group_list()) == 0:
        app.group.create(group_s)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, group_s)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == \
               sorted(app.group.get_contact_list(), key=Group.id_or_max)


def test_modify_group_footer(app, db, check_ui):
    group_s = Group(footer="test")
    if len(db.get_group_list()) == 0:
        app.group.create(group_s)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, group_s)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == \
               sorted(app.group.get_contact_list(), key=Group.id_or_max)
