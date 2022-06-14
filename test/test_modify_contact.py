#! /usr/bin/env python# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random


def test_modify_contact_fullname(app, db, check_ui):
    contact = Contact(firstname="Some test Name", lastname="Some lastname new")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    id = random_contact.id
    contact.id = id
    app.contact.modify_contact_by_id(random_contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    for i in range(len(old_contacts)):
        if old_contacts[i].id == random_contact.id:
            old_contacts[i] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_modify_contact_fullname_ui(app):
    contact = Contact(firstname="Some test Name", lastname="Some lastname new")
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_company_ui(app, db, check_ui):
    contact_s = Contact(company="New CompanyName")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact_s)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, contact_s)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert len(old_contacts) == app.contact.count()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
