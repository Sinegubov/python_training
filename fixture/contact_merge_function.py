import re


class ContactInfoHelper:

    def __init__(self, app):
        self.app = app

    def clear_phone(self, s):
        return re.sub("[()',. -]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear_phone(x), filter(lambda x: x is not None, [
                                    contact.home_telephone, contact.mobile_telephone, contact.work_telephone,
                                    contact.phone_home_secondary]))))

    def merge_email_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "", (filter(lambda x: x is not None,
                                                           [contact.email, contact.email2, contact.email3]))))
