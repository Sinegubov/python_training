# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact_fullname(app, db, check_ui):
    contact_s = Contact(firstname="Some test Name", lastname="Some lastname new")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact_s)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, contact_s)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_modify_contact_company(app, db, check_ui):
    contact_s = Contact(company="New CompanyName")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact_s)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, contact_s)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
