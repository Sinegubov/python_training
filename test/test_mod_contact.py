# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="new", middlename="new", lastname="new", nickname="new",
                                     title="new", company="new", address="new", home_telephone="new",
                                     mobile_telephone="new", work_telephone="new", fax="new", email="new",
                                     email2="new", email3="new", homepage="new,", address_secondary="new",
                                     phone_home_secondary="new", notes="new"))
    app.session.logout()
