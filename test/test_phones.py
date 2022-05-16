import re


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="234", lastname="qwer", home_telephone="xcvb",
                      mobile_telephone="tyui", work_telephone="ghj", phone_home_secondary="tgtgt"))
    contact_from_home_page = app.contact.get_contact_list_for_phones()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home_telephone == clear(contact_from_edit_page.home_telephone)
    assert contact_from_home_page.mobile_telephone == clear(contact_from_edit_page.mobile_telephone)
    assert contact_from_home_page.work_telephone == clear(contact_from_edit_page.work_telephone)
    assert contact_from_home_page.phone_home_secondary == clear(contact_from_edit_page.phone_home_secondary)

def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="234", lastname="qwer", home_telephone="xcvb",
                      mobile_telephone="tyui", work_telephone="ghj", phone_home_secondary="tgtgt"))
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_telephone == contact_from_edit_page.home_telephone
    assert contact_from_view_page.mobile_telephone == contact_from_edit_page.mobile_telephone
    assert contact_from_view_page.work_telephone == contact_from_edit_page.work_telephone
    assert contact_from_view_page.phone_home_secondary == contact_from_edit_page.phone_home_secondary

def clear(s):
    return re.sub("[() -]", "", s)
