# -*- coding: utf-8 -*-
import random
import data.contact
import data.groups


def test_add_contact_to_group(app, orm):
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
    # add_to_group, contact = orm.group_not_in_groups(all_groups, contact)
    if contact not in db_contacts_in_group:
        app.contact.add_contact_to_group(contact, group)
    else:
        if db_contacts_not_in_group:
            contact = random.choice(db_contacts_not_in_group)
            app.contact.add_contact_to_group(contact, group)
        else:
            if not db_contacts_not_in_group:
                contact = app.contact.create(data.contact.testdata[0])
                app.contact.add_contact_to_group(contact, group)
    old_list_contacts = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    new_list_contacts = orm.get_contacts_in_group(group)
    assert len(old_list_contacts) + 1 == len(new_list_contacts) and new_list_contacts.count(contact) == 1


def test_del_contact_from_group(app, orm):
    contact = None
    all_groups = orm.get_group_list()
    if len(all_groups) == 0:
        app.group.create(data.groups.testdata[1])
        app.contact.add_contact_to_group(random.choice(orm.get_contact_list()), random.choice(orm.get_group_list()))
        all_groups = orm.get_group_list()
    add_to_group, contact = orm.group_in_groups(all_groups, contact)
    if contact is None and orm.get_contact_list() == 0:
        app.contact.create(data.contact.testdata[1])
        contact = orm.get_contact_list()[0]
        add_to_group = random.choice(orm.get_group_list())
        app.contact.add_contact_to_group(contact, add_to_group)
    elif contact is None and orm.get_contact_list() != 0:
        contact = random.choice(orm.get_contact_list())
        add_to_group = random.choice(orm.get_group_list())
        app.contact.add_random_contact_to_random_group(contact, add_to_group)
    old_list_contacts = orm.get_contacts_in_group(add_to_group)
    app.contact.del_contact_from_group(contact, add_to_group)
    new_list_contacts = orm.get_contacts_in_group(add_to_group)
    assert len(old_list_contacts) - 1 == len(new_list_contacts) and new_list_contacts.count(contact) == 0
