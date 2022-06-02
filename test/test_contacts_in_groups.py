# -*- coding: utf-8 -*-
import random
from fixture.orm import ORMFixture


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    groups_in_db = db.get_group_list()
    group = str((random.choice(groups_in_db)).id)
    contacts_in_db = db.get_contact_list()
    contact = random.choice(contacts_in_db)
    app.contact.select_contact_by_id(contact.id)
    app.group.select_group_select(group)
    contacts_in_group_db = ORMFixture.get_contacts_in_group(groups_in_db)
    assert (contact in contacts_in_group_db)


# def test_add_contact_to_group(app):
#     contact=app.contact.select_contact(0)
#    app.group.select_group_from_dropdown(2)
#    contacts_in_group_db = ORMFixture.get_contacts_in_group()
#    assert(contact in contacts_in_group_db)


#def test_add_contact_to_group(app, db):
#    group_with_contacts = db.get_group_list()
#    if len(group_with_contacts) == 0:
#        app.contact.add_contact_to_group(contact.id)


