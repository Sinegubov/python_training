# -*- coding: utf-8 -*-
import random
import data.contact
import data.groups


def test_add_contact_to_group(app, db, orm):
    all_groups = orm.get_group_list()
    all_contacts = orm.get_contact_list()
    if not all_groups:
        app.group.create(data.groups.testdata[0])
        all_groups = orm.get_group_list()
    if not all_contacts:
        app.contact.create(data.contact.testdata[0])
        all_contacts = orm.get_contact_list()
    group = random.choice(all_groups)
    contact = random.choice(all_contacts)
    db_contacts_in_group = orm.get_contacts_in_group(group)
    db_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    if contact not in db_contacts_in_group:
        app.contact.add_contact_to_group(contact, group)
    else:
        if db_contacts_not_in_group:
            contact = random.choice(db_contacts_not_in_group)
            app.contact.add_contact_to_group(contact, group)
        else:
            if not db_contacts_not_in_group:
                app.contact.create(data.contact.testdata[0])
                contact = db.get_contact_list()[-1]
                app.contact.add_contact_to_group(contact, group)
    app.contact.add_contact_to_group(contact, group)
    new_list_contacts = orm.get_contacts_in_group(group)
    assert contact in new_list_contacts
    assert len(db_contacts_in_group) + 1 == len(new_list_contacts)


def test_del_contact_from_group(app, db, orm):
    all_groups = db.get_group_list()
    all_contacts = db.get_contact_list()
    if not all_groups:
        app.group.create(data.groups.testdata[1])
        all_groups = orm.get_group_list()
    if not all_contacts:
        app.contact.create(data.contact.testdata[1])
        all_contacts = orm.get_contact_list()
    group = random.choice(all_groups)
    contact = random.choice(all_contacts)
    db_contacts_in_group = orm.get_contacts_in_group(group)
    db_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    if contact not in db_contacts_in_group:
        app.contact.add_contact_to_group(contact, group)
    else:
        if db_contacts_not_in_group:
            contact = random.choice(db_contacts_not_in_group)
            app.contact.add_contact_to_group(contact, group)
        else:
            if not db_contacts_not_in_group:
                app.contact.create(data.contact.testdata[0])
                contact = db.get_contact_list()[-1]
                app.contact.add_contact_to_group(contact, group)
    # contact = random.choice(db_contacts_in_group)
    old_list_contacts = orm.get_contacts_in_group(group)
    app.contact.del_contact_from_group(contact, group)
    new_list_contacts = orm.get_contacts_in_group(group)
    assert contact not in new_list_contacts
    assert len(old_list_contacts) - 1 == len(new_list_contacts)
