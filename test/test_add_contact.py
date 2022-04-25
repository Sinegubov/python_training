# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="234", middlename="123", lastname="qwer", nickname="asdf",
                       title="zxczv", company="erty", address="dfgh", home_telephone="xcvb",
                       mobile_telephone="tyui", work_telephone="ghj", fax="mnbv", email="[iop", email2="jhkl",
                       email3="uiop", homepage="bnm,", address_secondary="5t5t5", phone_home_secondary="tgtgt",
                       notes="vfvfv"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                       address="", home_telephone="", mobile_telephone="", work_telephone="", fax="", email="",
                       email2="", email3="", homepage="", address_secondary="", phone_home_secondary="", notes=""))
    app.logout()
