# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.modify_first_contact(Contact(firstname="Some test Name"))
    app.contact.modify_first_contact(Contact(firstname="New FirstName"))


def test_modify_contact_company(app):
    if app.contact.count() == 0:
        app.contact.modify_first_contact(Contact(company="Some test Name"))
    app.contact.modify_first_contact(Contact(company="New CompanyName"))
