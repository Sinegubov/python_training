# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.modify_first_contact(Contact(firstname="Some test Name"))
    app.contact.delete_first_contact()
