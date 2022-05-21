from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    home_telephone="", mobile_telephone="", work_telephone="", fax="", email="", email2="", email3="",
                    homepage="", address_secondary="", phone_home_secondary="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename="", lastname=random_string("lastname", 10),
            nickname="", title="", company="", address=random_string("address", 20),
            home_telephone=random_string("home_telephone", 20), mobile_telephone=random_string("mobile_telephone", 20),
            work_telephone=random_string("work_telephone", 20), fax="", email=random_string("email", 20),
            email2=random_string("email2", 20), email3=random_string("email3", 20), homepage="", address_secondary="",
            phone_home_secondary="", notes="")
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
