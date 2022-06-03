import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list_groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list_groups.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list_groups

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_list_full(self):
        list_contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                all_phones = home + mobile + work + phone2
                all_mail = email + email2 + email3
                list_contacts.append(Contact(id=str(id), firstname=firstname.strip(), lastname=lastname.strip(), address=address,
                                             home_telephone=home.strip(), mobile_telephone=mobile.strip(), work_telephone=work.strip(),
                                             phone_home_secondary=phone2.strip(), email=email.strip(), email2=email2.strip(), email3=email3.strip(),
                                             all_email_from_home_page=all_mail.strip(), all_phones_from_home_page=all_phones.strip()))
        finally:
            cursor.close()
        return list_contacts

    def destroy(self):
        self.connection.close()
