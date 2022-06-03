# -*- coding: utf-8 -*-
from model.contact import Contact


def test_matches_contacts_on_db_and_homepage(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Some test Name", lastname="Some lastname new"))
    contacts_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_db = sorted(db.get_contact_list_full(), key=Contact.id_or_max)
    for i in range(len(contacts_db)):
        assert contacts_ui[i].lastname == contacts_db[i].lastname
        assert contacts_ui[i].firstname == contacts_db[i].firstname
        assert contacts_ui[i].address == contacts_db[i].address
        assert contacts_ui[i].all_email_from_home_page == \
               app.contact_merge_function.merge_email_like_on_home_page(contacts_db[i])
        assert contacts_ui[i].all_phones_from_home_page == \
               app.contact_merge_function.merge_phones_like_on_home_page(contacts_db[i])
