from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements(by=By.NAME, value="submit")) > 0):
            wd.find_element(by=By.LINK_TEXT, value="add new").click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_telephone)
        self.change_field_value("mobile", contact.mobile_telephone)
        self.change_field_value("work", contact.work_telephone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone_home_secondary)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(by=By.NAME, value=field_name).click()
            wd.find_element(by=By.NAME, value=field_name).clear()
            wd.find_element(by=By.NAME, value=field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # Fill contact form
        self.fill_contact_form(contact)
        # Submit contact creation
        wd.find_element(by=By.NAME, value="submit").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def return_to_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and wd.find_elements(by=By.NAME, value="Send e-Mail")):
            wd.find_element(by=By.LINK_TEXT, value="home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_first_contact()
        # Submit deletion
        wd.find_element(by=By.XPATH, value="//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_contact_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(by=By.NAME, value="selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_contact_page()
        # Submit edit button for first contact
        wd.find_element(by=By.XPATH, value="//img[@alt='Edit']").click()
        # Fill contact form
        self.fill_contact_form(new_contact_data)
        # Submit update button for contact
        wd.find_element(by=By.NAME, value="update").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.return_to_contact_page()
        return len(wd.find_elements(by=By.NAME, value="selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_contact_page()
            self.contact_cache = []
            for element in wd.find_elements(by=By.NAME, value="entry"):
                text_firstname = element.find_element(by=By.CSS_SELECTOR, value="td:nth-child(3)").text
                text_lasttname = element.find_element(by=By.CSS_SELECTOR, value="td:nth-child(2)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=text_firstname, lastname=text_lasttname, id=id))
        return list(self.contact_cache)
