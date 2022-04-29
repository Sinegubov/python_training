# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New FirstName"))
    app.session.logout()


def test_mod_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(company="New CompanyName"))
    app.session.logout()
