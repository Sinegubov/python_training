# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        wd = self.wd
        wd.get("http://nb0660.local/addressbook/index.php")
        wd.find_element(by=By.NAME,value="user").click()
        wd.find_element(by=By.NAME,value="user").clear()
        wd.find_element(by=By.NAME,value="user").send_keys("admin")
        wd.find_element(by=By.NAME,value="pass").clear()
        wd.find_element(by=By.NAME,value="pass").send_keys("secret")
        wd.find_element(by=By.XPATH,value="//input[@value='Login']").click()
        wd.find_element(by=By.LINK_TEXT,value="groups").click()
        wd.find_element(by=By.NAME,value="new").click()
        wd.find_element(by=By.NAME,value="group_name").click()
        wd.find_element(by=By.NAME,value="group_name").clear()
        wd.find_element(by=By.NAME,value="group_name").send_keys("asdasd")
        wd.find_element(by=By.NAME,value="group_header").click()
        wd.find_element(by=By.NAME,value="group_header").clear()
        wd.find_element(by=By.NAME,value="group_header").send_keys("asdasd")
        wd.find_element(by=By.NAME,value="group_footer").click()
        wd.find_element(by=By.NAME,value="group_footer").clear()
        wd.find_element(by=By.NAME,value="group_footer").send_keys("asdasdasdasd")
        wd.find_element(by=By.NAME,value="submit").click()
        wd.find_element(by=By.LINK_TEXT,value="group page").click()
        wd.find_element(by=By.LINK_TEXT,value="Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to.alert.text()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
