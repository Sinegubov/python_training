# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_group_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()

try:
    r = app.group.get_contact_list()
    for item in r:
        print(item)
    print(len(r))
finally:
    pass  # db.destroy()
