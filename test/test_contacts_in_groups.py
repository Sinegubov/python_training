# -*- coding: utf-8 -*-
import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, orm):
    contact = None
    # add_to_group = None
    all_groups = orm.get_group_list()
    if len(all_groups) == 0:
        app.group.create(Group(name="SomeName", header="SomeHeader", footer="SomeFooter"))
        all_groups = orm.get_group_list()
        group = all_groups[len(all_groups)-1]
    if contact is None:
        app.contact.create(Contact(firstname="name1", middlename="middl", lastname="lasst", nickname="nick", title="T",
                                   company="Apple", address="Earth", home_telephone="12332123",
                                   mobile_telephone="3454345", work_telephone="5676567", fax="44444444",
                                   email="asd@asd.ASd", email2="qwe_ewq@w.w.w.e", email3="email",
                                   homepage="http://asd.asd", address_secondary="MilkyWay",
                                   phone_home_secondary="876867876", notes="zzzz"))
        contacts = sorted(orm.get_contact_list(), key=Contact.id_or_max)
        contact = contacts[len(contacts)-1]
    for group in all_groups:
        contacts = orm.get_contacts_not_in_group(group)
        if len(contacts) > 0:
            contact = contacts[0]
            add_to_group = group
            break
    old_list_contacts = orm.get_contacts_in_group(add_to_group)
    app.contact.add_contact_to_group(contact, add_to_group)
    new_list_contacts = orm.get_contacts_in_group(add_to_group)
    assert len(old_list_contacts) + 1 == len(new_list_contacts) and new_list_contacts.count(contact) == 1


def test_del_contact_from_group(app, orm):
    contact = None
    # add_to_group = None
    all_groups = orm.get_group_list()
    if len(all_groups) == 0:
        app.group.create(Group(name="SomeName", header="SomeHeader", footer="SomeFooter"))
        app.contact.add_contact_to_group(random.choice(orm.get_contact_list()), random.choice(orm.get_group_list()))
        all_groups = orm.get_group_list()
    for group in all_groups:
        contacts = orm.get_contacts_in_group(group)
        if len(contacts) > 0:
            contact = contacts[0]
            add_to_group = group
            break
    if contact is None and orm.get_contact_list() == 0:
        app.contact.create(Contact(firstname="name2", middlename="midd2", lastname="lasst", nickname="nick", title="T",
                           company="Apple", address="Earth", home_telephone="12332123",
                           mobile_telephone="3454345", work_telephone="5676567", fax="44444444",
                           email="asd@asd.ASd", email2="qwe_ewq@w.w.w.e", email3="email",
                           homepage="http://asd.asd", address_secondary="MilkyWay",
                           phone_home_secondary="876867876", notes="zzzz"))
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
