import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list_for_phones()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_telephone == contact_from_edit_page.home_telephone
    assert contact_from_view_page.mobile_telephone == contact_from_edit_page.mobile_telephone
    assert contact_from_view_page.work_telephone == contact_from_edit_page.work_telephone
    assert contact_from_view_page.phone_home_secondary == contact_from_edit_page.phone_home_secondary


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home_telephone, contact.mobile_telephone,
                                                            contact.work_telephone, contact.phone_home_secondary]))))
