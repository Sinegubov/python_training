from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(by=By.NAME, value="new")) > 0):
            wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(by=By.NAME, value=field_name).click()
            wd.find_element(by=By.NAME, value=field_name).clear()
            wd.find_element(by=By.NAME, value=field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # Init group creation
        wd.find_element(by=By.NAME, value="new").click()
        # Fill group form
        self.fill_group_form(group)
        # submit groups creation
        wd.find_element(by=By.NAME, value="submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(by=By.NAME, value="new")) > 0):
            wd.find_element(by=By.LINK_TEXT, value="group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # Submit deletion
        wd.find_element(by=By.NAME, value="delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(by=By.NAME, value="selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # Open modification form
        wd.find_element(by=By.NAME, value="edit").click()
        # Fill group form
        self.fill_group_form(new_group_data)
        # Submit modification
        wd.find_element(by=By.NAME, value="update").click()
        self.return_to_groups_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(by=By.NAME, value="selected[]"))