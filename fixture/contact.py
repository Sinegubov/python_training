from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        # Open page for add address book entry
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

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element(by=By.LINK_TEXT, value="home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_first_contact()
        # Submit deletion
        wd.find_element(by=By.XPATH, value="//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_contact_page()

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

    def count(self):
        wd = self.app.wd
        self.return_to_contact_page()
        return len(wd.find_elements(by=By.NAME, value="selected[]"))
