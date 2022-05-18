# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="234", middlename="123", lastname="qwer", nickname="asdf",
                      title="zxczv", company="erty", address="dfgh", home_telephone="xcvb",
                      mobile_telephone="tyui", work_telephone="ghj", fax="mnbv", email="[iop", email2="jhkl",
                      email3="uiop", homepage="bnm,", address_secondary="5t5t5", phone_home_secondary="tgtgt",
                      notes="vfvfv")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
#                      address="", home_telephone="", mobile_telephone="", work_telephone="", fax="", email="",
#                      email2="", email3="", homepage="", address_secondary="", phone_home_secondary="",
#                      notes="")
#    app.contact.create(contact)
#    assert len(old_contacts) + 1 == app.contact.count()
#    new_contacts = app.contact.get_contact_list()
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
