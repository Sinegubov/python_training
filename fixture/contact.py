from selenium.webdriver.common.by import By
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements(by=By.NAME, value="submit")) > 0):
            wd.find_element(by=By.LINK_TEXT, value="add new").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements(by=By.NAME, value="entry")[index]
        cell = element.find_elements(by=By.TAG_NAME, value="td")[7]
        cell.find_element(by=By.TAG_NAME, value="a").click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements(by=By.NAME, value="entry")[index]
        cell = element.find_elements(by=By.TAG_NAME, value="td")[7]
        cell.find_element(by=By.TAG_NAME, value="a").click()

    def return_to_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and wd.find_elements(by=By.NAME, value="Send e-Mail")):
            wd.find_element(by=By.LINK_TEXT, value="home").click()

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

    contact_cache = None

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # Fill contact form
        self.fill_contact_form(contact)
        # Submit contact creation
        wd.find_element(by=By.NAME, value="submit").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def add_contact_to_group(self, contact, add_to_group):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_contact_by_id(contact.id)
        wd.find_element_by_css_selector('select[name="to_group"]').click()
        wd.find_element_by_css_selector('select[name="to_group"] option[value="%s"]' % add_to_group.id).click()
        wd.find_element_by_css_selector('input[value="Add to"]').click()
        self.return_to_contact_page()

    def select_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element(by=By.NAME, value="selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(by=By.NAME, value="selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(by=By.CSS_SELECTOR, value="input[id='%s']" % id).click()

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_contact_by_id(id)
        # Submit edit button for random contact
        wd.find_element(by=By.XPATH, value="//td/a[contains(@href, '%s')]/img[@title='Edit']" % id).click()
        # Fill contact form
        self.fill_contact_form(contact)
        # Submit update button for contact
        wd.find_element(by=By.NAME, value="update").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_contact_by_index(index)
        # Submit edit button for first contact
        wd.find_elements(by=By.XPATH, value="//img[@alt='Edit']")[index].click()
        # Fill contact form
        self.fill_contact_form(contact)
        # Submit update button for contact
        wd.find_element(by=By.NAME, value="update").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact_s):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_contact_by_id(id)
        # Submit edit button for first contact
        wd.find_element(by=By.XPATH, value="//img[@alt='Edit']").click()
        # Fill contact form
        self.fill_contact_form(contact_s)
        # Submit update button for contact
        wd.find_element(by=By.NAME, value="update").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.return_to_contact_page()
        return len(wd.find_elements(by=By.NAME, value="selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_contact_page()
            self.contact_cache = []
            for element in wd.find_elements(by=By.XPATH, value="//tr[position() >1]"):
                firstname = element.find_element(by=By.XPATH, value=".//td[3]").text.strip()
                lastname = element.find_element(by=By.XPATH, value=".//td[2]").text.strip()
                address = element.find_element(by=By.XPATH, value=".//td[4]").text.strip()
                id = element.find_element(by=By.XPATH, value=".//td/input[@type='checkbox']").get_attribute("value")
                all_phones = element.find_element(by=By.XPATH, value=".//td[6]").text.strip()
                all_email = element.find_element(by=By.XPATH, value=".//td[5]").text.strip()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_email))

        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(by=By.NAME, value="firstname").get_attribute("value")
        lastname = wd.find_element(by=By.NAME, value="lastname").get_attribute("value")
        id = wd.find_element(by=By.NAME, value="id").get_attribute("value")
        address = wd.find_element(by=By.NAME, value="address").get_attribute("value")
        email = wd.find_element(by=By.NAME, value="email").get_attribute("value")
        email2 = wd.find_element(by=By.NAME, value="email2").get_attribute("value")
        email3 = wd.find_element(by=By.NAME, value="email3").get_attribute("value")
        home_telephone = wd.find_element(by=By.NAME, value="home").get_attribute("value")
        mobile_telephone = wd.find_element(by=By.NAME, value="mobile").get_attribute("value")
        work_telephone = wd.find_element(by=By.NAME, value="work").get_attribute("value")
        phone_home_secondary = wd.find_element(by=By.NAME, value="phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home_telephone=home_telephone,
                       mobile_telephone=mobile_telephone, work_telephone=work_telephone,
                       phone_home_secondary=phone_home_secondary, address=address, email=email, email2=email2,
                       email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element(by=By.ID, value="content").text
        home_telephone = re.search("H: (.*)", text).group(1)
        mobile_telephone = re.search("M: (.*)", text).group(1)
        work_telephone = re.search("W: (.*)", text).group(1)
        phone_home_secondary = re.search("P: (.*)", text).group(1)
        return Contact(home_telephone=home_telephone,
                       mobile_telephone=mobile_telephone, work_telephone=work_telephone,
                       phone_home_secondary=phone_home_secondary)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_contact_by_id(id)
        # Submit deletion
        wd.find_element(by=By.XPATH, value="//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_contact_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_contact_by_index(index)
        # Submit deletion
        wd.find_element(by=By.XPATH, value="//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_contact_page()
        self.contact_cache = None

    def del_contact_from_group(self, contact, group):
        wd = self.app.wd
        self.return_to_contact_page()
        wd.find_element_by_css_selector('select[name="group"]').click()
        wd.find_element_by_css_selector('select[name="group"] option[value="%s"]' % group.id).click()
        id = contact.id
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector('input[name="remove"]').click()
