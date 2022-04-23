from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element(by=By.NAME, value="user").click()
        wd.find_element(by=By.NAME, value="user").clear()
        wd.find_element(by=By.NAME, value="user").send_keys(username)
        wd.find_element(by=By.NAME, value="pass").click()
        wd.find_element(by=By.NAME, value="pass").clear()
        wd.find_element(by=By.NAME, value="pass").send_keys(password)
        wd.find_element(by=By.XPATH, value="//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # Init group creation
        wd.find_element(by=By.NAME, value="new").click()
        # Fill group form
        wd.find_element(by=By.NAME, value="group_name").click()
        wd.find_element(by=By.NAME, value="group_name").clear()
        wd.find_element(by=By.NAME, value="group_name").send_keys(group.name)
        wd.find_element(by=By.NAME, value="group_header").click()
        wd.find_element(by=By.NAME, value="group_header").clear()
        wd.find_element(by=By.NAME, value="group_header").send_keys(group.header)
        wd.find_element(by=By.NAME, value="group_footer").click()
        wd.find_element(by=By.NAME, value="group_footer").clear()
        wd.find_element(by=By.NAME, value="group_footer").send_keys(group.footer)
        # submit groups creation
        wd.find_element(by=By.NAME, value="submit").click()
        self.return_to_groups_page()

    def open_contact_page(self):
        wd = self.wd
        # Open page for add address book entry
        wd.find_element(by=By.LINK_TEXT, value="add new").click()

    def create_contact(self, contact):
        wd = self.wd
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
        wd = self.wd
        wd.find_element(by=By.LINK_TEXT, value="home").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element(by=By.LINK_TEXT, value="group page").click()

    def logout(self):
        wd = self.wd
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def destroy(self):
        self.wd.quit()
