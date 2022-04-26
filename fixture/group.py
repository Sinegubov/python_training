from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def create(self, group):
        wd = self.app.wd
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

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(by=By.LINK_TEXT, value="group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # Select first group
        wd.find_element(by=By.NAME, value="selected[]").click()
        # Submit deletion
        wd.find_element(by=By.NAME, value="delete").click()
        self.return_to_groups_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # Select first group
        wd.find_element(by=By.NAME, value="selected[]").click()
        # Submit edit button
        wd.find_element(by=By.NAME, value="edit").click()
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
        # submit groups modification
        wd.find_element(by=By.NAME, value="update").click()
        self.return_to_groups_page()
