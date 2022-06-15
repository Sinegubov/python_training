# -*- coding: utf-8 -*-
import random
import data.contact
import data.groups


def test_add_contact_to_group(app, db, orm):
    if not orm.get_group_list():
        app.group.create(data.groups.testdata[0])
    if not orm.get_contact_list():
        app.contact.create(data.contact.testdata[0])
    contact, group, old_list_contacts_in_group = app.contact.check_and_add_contact_to_group(orm, db)
    new_list_contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in orm.get_contacts_in_group(group)
    assert len(old_list_contacts_in_group) + 1 == len(new_list_contacts_in_group)


def test_del_contact_from_group(app, db, orm):
    if not orm.get_group_list():
        app.group.create(data.groups.testdata[0])
    if not orm.get_contact_list():
        app.contact.create(data.contact.testdata[0])
    group = random.choice(orm.get_group_list())
    db_contacts_in_group = orm.get_contacts_in_group(group)
    if db_contacts_in_group:
        contact = random.choice(db_contacts_in_group)
        app.contact.del_contact_from_group(contact, group)
    else:
        contact, group, old_list_contacts_in_group = app.contact.check_and_add_contact_to_group(orm, db)
        app.contact.del_contact_from_group(contact, group)
    new_list_contacts = orm.get_contacts_in_group(group)
    assert contact not in new_list_contacts

