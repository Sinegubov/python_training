# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_contact_info_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="name2", middlename="midd2", lastname="las2t", nickname="nick2",
                                   title="T2", company="Apple2", address="Earth2", home_telephone="123321232",
                                   mobile_telephone="34543452", work_telephone="56765672", fax="444444442",
                                   email="asd@asd.ASd2", email2="qwe_ewq@w.w.w.2", email3="email2",
                                   homepage="http://222.asd", address_secondary="MilkyWay2",
                                   phone_home_secondary="8768678762", notes="zzzzyyy"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_email_from_home_page == \
           app.contact_merge_function.merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == \
           app.contact_merge_function.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
