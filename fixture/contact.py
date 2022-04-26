from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        # Open page for add address book entry
        wd.find_element(by=By.LINK_TEXT, value="add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # Fill contact form
        wd.find_element(by=By.NAME, value="firstname").clear()
        wd.find_element(by=By.NAME, value="firstname").send_keys(contact.firstname)
        wd.find_element(by=By.NAME, value="middlename").clear()
        wd.find_element(by=By.NAME, value="middlename").send_keys(contact.middlename)
        wd.find_element(by=By.NAME, value="lastname").clear()
        wd.find_element(by=By.NAME, value="lastname").send_keys(contact.lastname)
        wd.find_element(by=By.NAME, value="nickname").clear()
        wd.find_element(by=By.NAME, value="nickname").send_keys(contact.nickname)
        wd.find_element(by=By.NAME, value="title").clear()
        wd.find_element(by=By.NAME, value="title").send_keys(contact.title)
        wd.find_element(by=By.NAME, value="company").clear()
        wd.find_element(by=By.NAME, value="company").send_keys(contact.company)
        wd.find_element(by=By.NAME, value="address").clear()
        wd.find_element(by=By.NAME, value="address").send_keys(contact.address)
        wd.find_element(by=By.NAME, value="home").clear()
        wd.find_element(by=By.NAME, value="home").send_keys(contact.home_telephone)
        wd.find_element(by=By.NAME, value="mobile").clear()
        wd.find_element(by=By.NAME, value="mobile").send_keys(contact.mobile_telephone)
        wd.find_element(by=By.NAME, value="work").clear()
        wd.find_element(by=By.NAME, value="work").send_keys(contact.work_telephone)
        wd.find_element(by=By.NAME, value="fax").clear()
        wd.find_element(by=By.NAME, value="fax").send_keys(contact.fax)
        wd.find_element(by=By.NAME, value="email").clear()
        wd.find_element(by=By.NAME, value="email").send_keys(contact.email)
        wd.find_element(by=By.NAME, value="email2").clear()
        wd.find_element(by=By.NAME, value="email2").send_keys(contact.email2)
        wd.find_element(by=By.NAME, value="email3").clear()
        wd.find_element(by=By.NAME, value="email3").send_keys(contact.email3)
        wd.find_element(by=By.NAME, value="homepage").clear()
        wd.find_element(by=By.NAME, value="homepage").send_keys(contact.homepage)
        wd.find_element(by=By.NAME, value="address2").clear()
        wd.find_element(by=By.NAME, value="address2").send_keys(contact.address2)
        wd.find_element(by=By.NAME, value="phone2").clear()
        wd.find_element(by=By.NAME, value="phone2").send_keys(contact.phone_home_secondary)
        wd.find_element(by=By.NAME, value="notes").clear()
        wd.find_element(by=By.NAME, value="notes").send_keys(contact.notes)
        # Submit contact creation
        wd.find_element(by=By.NAME, value="submit").click()
        self.return_to_contact_page()

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element(by=By.LINK_TEXT, value="home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_contact_page()
        # Select first group
        wd.find_element(by=By.NAME, value="selected[]").click()
        # Submit deletion
        wd.find_element(by=By.XPATH, value="//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
