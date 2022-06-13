# -*- coding: utf-8 -*-
from splinter import Browser
from contact import Contact
import unittest


class TestAddContactSplinter(unittest.TestCase):
    def setUp(self):
        self.browser = Browser('firefox', headless=True)

    def open_home_page(self, browser):
        browser.visit("http://localhost/addressbook/")

    def login(self, browser, username, password):
        browser.fill('user', username)
        browser.fill('pass', password)
        browser.find_by_xpath("//input[@value='Login']").click()

    def open_contact_page(self, browser):
        # Open page for add address book entry
        browser.visit("http://localhost/addressbook/edit.php")

    def create_contact(self, browser, contact):
        # Fill contact form
        browser.fill("firstname", contact.firstname)
        browser.fill("middlename", contact.middlename)
        browser.fill("lastname", contact.lastname)
        browser.fill("nickname", contact.nickname)
        browser.fill("title", contact.title)
        browser.fill("company", contact.company)
        browser.fill("address", contact.address)
        browser.fill("home", contact.home_telephone)
        browser.fill("mobile", contact.mobile_telephone)
        browser.fill("work", contact.work_telephone)
        browser.fill("fax", contact.fax)
        browser.fill("email", contact.email)
        browser.fill("email2", contact.email2)
        browser.fill("email3", contact.email3)
        browser.fill("homepage", contact.homepage)
        browser.fill("address2", contact.address2)
        browser.fill("phone2", contact.phone_home_secondary)
        browser.fill("notes", contact.notes)
        # Submit contact creation
        browser.find_by_name("submit").click()

    def return_to_contact_page(self, browser):
        browser.find_by_text("home").click()

    def logout(self, browser):
        browser.find_by_text("Logout").click()

    def test_add_contact(self):
        browser = self.browser
        self.open_home_page(browser)
        self.login(browser, username="admin", password="secret")
        self.open_contact_page(browser)
        self.create_contact(browser, Contact(firstname="234", middlename="123", lastname="qwer", nickname="asdf",
                            title="zxczv", company="erty", address="dfgh", home_telephone="xcvb",
                            mobile_telephone="tyui", work_telephone="ghj", fax="mnbv", email="[iop", email2="jhkl",
                            email3="uiop", homepage="bnm,", address_secondary="5t5t5", phone_home_secondary="tgtgt",
                            notes="vfvfv"))
        self.return_to_contact_page(browser)
        self.logout(browser)

    def test_add_empty_contact(self):
        browser = self.browser
        self.open_home_page(browser)
        self.login(browser, username="admin", password="secret")
        self.open_contact_page(browser)
        self.create_contact(browser, Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                            address="", home_telephone="", mobile_telephone="", work_telephone="", fax="", email="",
                            email2="", email3="", homepage="", address_secondary="", phone_home_secondary="", notes=""))
        self.return_to_contact_page(browser)
        self.logout(browser)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
