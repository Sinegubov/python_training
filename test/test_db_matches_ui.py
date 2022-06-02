# -*- coding: utf-8 -*-
from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group_ui = app.group.get_group_list()
    print(timeit(lambda: group_ui, number=1))

    def clean(group):
        return Group(id=group.id.strip(), name=group.name.strip())
    group_db = map(clean, db.get_group_list())
    print(timeit(lambda: group_db, number=1))
    assert sorted(group_ui, key=Group.id_or_max) == sorted(group_db, key=Group.id_or_max)
