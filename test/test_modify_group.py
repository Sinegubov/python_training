# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    group = Group(name="New group")
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    id = random_group.id
    group.id = id
    app.group.modify_group_by_id(random_group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    for i in range(len(old_groups)):
        if old_groups[i].id == random_group.id:
            old_groups[i] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
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
    assert len(old_groups) == app.group.count()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
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
    assert len(old_groups) == app.group.count()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == \
               sorted(app.group.get_contact_list(), key=Group.id_or_max)
