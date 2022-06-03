from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_telephone=None, mobile_telephone=None, work_telephone=None, fax=None, email=None,
                 email2=None, email3=None, homepage=None, address_secondary=None, phone_home_secondary=None,
                 notes=None, all_phones_from_home_page=None, all_email_from_home_page=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_telephone = home_telephone
        self.mobile_telephone = mobile_telephone
        self.work_telephone = work_telephone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address_secondary
        self.phone_home_secondary = phone_home_secondary
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s ; %s ; %s ; %s ; %s ; %s ; " \
               "%s ; %s ; %s ; %s ; %s" % (self.id, self.firstname, self.lastname, self.address, self.home_telephone,
                                           self.mobile_telephone, self.work_telephone, self.phone_home_secondary,
                                           self.email, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
