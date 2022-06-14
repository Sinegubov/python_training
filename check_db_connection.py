# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    list_l = db.get_group_list()
    for item in list_l:
        print(item)
    print(len(list_l))
finally:
    pass  # db.destroy()
