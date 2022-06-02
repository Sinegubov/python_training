# -*- coding: utf-8 -*-
from model.contact import Contact


def test_matches_contacts_on_db_and_homepage(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Some test Name", lastname="Some lastname new"))
    contacts_ui = app.contact.get_contact_list()
    contacts_db = db.get_contact_list_full()
    assert sorted(contacts_ui, key=Contact.id_or_max) == sorted(contacts_db, key=Contact.id_or_max)
