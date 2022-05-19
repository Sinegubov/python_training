# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    home_telephone="", mobile_telephone="", work_telephone="", fax="", email="", email2="", email3="",
                    homepage="", address_secondary="", phone_home_secondary="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename="", lastname=random_string("lastname", 10),
            nickname="", title="", company="", address=random_string("address", 20),
            home_telephone=random_string("home_telephone", 20), mobile_telephone=random_string("mobile_telephone", 20),
            work_telephone=random_string("work_telephone", 20), fax="", email=random_string("email", 20),
            email2=random_string("email2", 20), email3=random_string("email3", 20), homepage="", address_secondary="",
            phone_home_secondary="", notes="")
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
