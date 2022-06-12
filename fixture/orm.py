from pony.orm import *
from datetime import datetime

import fixture.contact
from model.group import Group
from fixture.contact import Contact

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups',
                       lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts',
                     lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(list(select(g for g in ORMFixture.ORMGroup)))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(list(select(c for c in ORMFixture.ORMContact if c.deprecated is None)))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            list(select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups)))

    @db_session
    def group_not_in_groups(self, all_groups, contact):
        for group in all_groups:
            contacts = self.get_contacts_not_in_group(group)
            if len(contacts) > 0:
                contact = contacts[0]
                add_to_group = group
                break
            else:
                contact = fixture.contact.ContactHelper.
                add_to_group = group
        return add_to_group, contact

    @db_session
    def group_in_groups(self, all_groups, contact):
        for group in all_groups:
            contacts = self.get_contacts_in_group(group)
            if len(contacts) > 0:
                contact = contacts[0]
                add_to_group = group
                break
        return add_to_group, contact
