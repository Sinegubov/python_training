# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element(by=By.NAME, value="user").clear()
        wd.find_element(by=By.NAME, value="user").send_keys(username)
        wd.find_element(by=By.NAME, value="pass").clear()
        wd.find_element(by=By.NAME, value="pass").send_keys(password)
        wd.find_element(by=By.XPATH, value="//input[@value='Login']").click()

    def open_contact_page(self, wd):
        # Open page for add address book entry
        wd.find_element(by=By.LINK_TEXT, value="add new").click()

    def create_contact(self, wd, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work,
                       fax, email, email3, email2, homepage, address2, phone2, notes):
        # Fill contact form
        wd.find_element(by=By.NAME, value="firstname").clear()
        wd.find_element(by=By.NAME, value="firstname").send_keys(firstname)
        wd.find_element(by=By.NAME, value="middlename").clear()
        wd.find_element(by=By.NAME, value="middlename").send_keys(middlename)
        wd.find_element(by=By.NAME, value="lastname").clear()
        wd.find_element(by=By.NAME, value="lastname").send_keys(lastname)
        wd.find_element(by=By.NAME, value="nickname").clear()
        wd.find_element(by=By.NAME, value="nickname").send_keys(nickname)
        wd.find_element(by=By.NAME, value="title").clear()
        wd.find_element(by=By.NAME, value="title").send_keys(title)
        wd.find_element(by=By.NAME, value="company").clear()
        wd.find_element(by=By.NAME, value="company").send_keys(company)
        wd.find_element(by=By.NAME, value="address").clear()
        wd.find_element(by=By.NAME, value="address").send_keys(address)
        wd.find_element(by=By.NAME, value="home").clear()
        wd.find_element(by=By.NAME, value="home").send_keys(home)
        wd.find_element(by=By.NAME, value="mobile").clear()
        wd.find_element(by=By.NAME, value="mobile").send_keys(mobile)
        wd.find_element(by=By.NAME, value="work").clear()
        wd.find_element(by=By.NAME, value="work").send_keys(work)
        wd.find_element(by=By.NAME, value="fax").clear()
        wd.find_element(by=By.NAME, value="fax").send_keys(fax)
        wd.find_element(by=By.NAME, value="email").clear()
        wd.find_element(by=By.NAME, value="email").send_keys(email)
        wd.find_element(by=By.NAME, value="email2").clear()
        wd.find_element(by=By.NAME, value="email2").send_keys(email2)
        wd.find_element(by=By.NAME, value="email3").clear()
        wd.find_element(by=By.NAME, value="email3").send_keys(email3)
        wd.find_element(by=By.NAME, value="homepage").clear()
        wd.find_element(by=By.NAME, value="homepage").send_keys(homepage)
        wd.find_element(by=By.NAME, value="address2").clear()
        wd.find_element(by=By.NAME, value="address2").send_keys(address2)
        wd.find_element(by=By.NAME, value="phone2").clear()
        wd.find_element(by=By.NAME, value="phone2").send_keys(phone2)
        wd.find_element(by=By.NAME, value="notes").clear()
        wd.find_element(by=By.NAME, value="notes").send_keys(notes)
        # Submit contact creation
        wd.find_element(by=By.NAME, value="submit").click()

    def return_to_contact_page(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="home").click()

    def logout(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.create_contact(wd, firstname="234", middlename="123", lastname="qwer", nickname="asdf", title="zxczv",
                            company="erty", address="dfgh", home="xcvb", mobile="tyui", work="ghj", fax="mnbv",
                            email="[iop", email2="jhkl", email3="uiop", homepage="bnm,", address2="5t5t5",
                            phone2="tgtgt", notes="vfvfv")
        self.return_to_contact_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.create_contact(wd, firstname="", middlename="", lastname="", nickname="", title="",
                            company="", address="", home="", mobile="", work="", fax="",
                            email="", email2="", email3="", homepage="", address2="",
                            phone2="", notes="")
        self.return_to_contact_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
