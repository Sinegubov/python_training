# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    contact = Contact(firstname="Some test Name", lastname="Some lastname new")
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_company(app):
    contact = Contact(company="New CompanyName")
    if app.contact.count() == 0:
        app.contact.create(Contact(company="Some test Name"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
