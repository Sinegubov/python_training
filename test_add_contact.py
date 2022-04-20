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

    def login(self, wd):
        wd.find_element(by=By.NAME, value="user").clear()
        wd.find_element(by=By.NAME, value="user").send_keys("admin")
        wd.find_element(by=By.NAME, value="pass").clear()
        wd.find_element(by=By.NAME, value="pass").send_keys("secret")
        wd.find_element(by=By.XPATH, value="//input[@value='Login']").click()

    def open_contact_page(self, wd):
        # Open page for add address book entry
        wd.find_element(by=By.LINK_TEXT, value="add new").click()

    def create_contact(self, wd):
        # Fill contact form
        wd.find_element(by=By.NAME, value="firstname").clear()
        wd.find_element(by=By.NAME, value="firstname").send_keys("234")
        wd.find_element(by=By.NAME, value="middlename").clear()
        wd.find_element(by=By.NAME, value="middlename").send_keys("123")
        wd.find_element(by=By.NAME, value="lastname").clear()
        wd.find_element(by=By.NAME, value="lastname").send_keys("qwer")
        wd.find_element(by=By.NAME, value="nickname").clear()
        wd.find_element(by=By.NAME, value="nickname").send_keys("asdf")
        wd.find_element(by=By.NAME, value="title").clear()
        wd.find_element(by=By.NAME, value="title").send_keys("zxczv")
        wd.find_element(by=By.NAME, value="company").clear()
        wd.find_element(by=By.NAME, value="company").send_keys("erty")
        wd.find_element(by=By.NAME, value="address").clear()
        wd.find_element(by=By.NAME, value="address").send_keys("dfgh")
        wd.find_element(by=By.NAME, value="home").clear()
        wd.find_element(by=By.NAME, value="home").send_keys("xcvb")
        wd.find_element(by=By.NAME, value="mobile").clear()
        wd.find_element(by=By.NAME, value="mobile").send_keys("tyui")
        wd.find_element(by=By.NAME, value="work").clear()
        wd.find_element(by=By.NAME, value="work").send_keys("ghj")
        wd.find_element(by=By.NAME, value="fax").clear()
        wd.find_element(by=By.NAME, value="fax").send_keys("mnbv")
        wd.find_element(by=By.NAME, value="email").clear()
        wd.find_element(by=By.NAME, value="email").send_keys("[iop")
        wd.find_element(by=By.NAME, value="email2").clear()
        wd.find_element(by=By.NAME, value="email2").send_keys("uiop")
        wd.find_element(by=By.NAME, value="email3").clear()
        wd.find_element(by=By.NAME, value="email3").send_keys("jhkl")
        wd.find_element(by=By.NAME, value="homepage").clear()
        wd.find_element(by=By.NAME, value="homepage").send_keys("bnm,")
        wd.find_element(by=By.NAME, value="address2").clear()
        wd.find_element(by=By.NAME, value="address2").send_keys("5t5t5")
        wd.find_element(by=By.NAME, value="phone2").clear()
        wd.find_element(by=By.NAME, value="phone2").send_keys("tgtgt")
        wd.find_element(by=By.NAME, value="notes").clear()
        wd.find_element(by=By.NAME, value="notes").send_keys("vfvfv")
        # Submit contact creation
        wd.find_element(by=By.NAME, value="submit").click()

    def return_to_contact_page(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="home").click()

    def logout(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_contact_page(wd)
        self.create_contact(wd)
        self.return_to_contact_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
