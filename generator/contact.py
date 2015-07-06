# -*- coding: utf-8 -*-

from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
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

def random_letters(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_year(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                    title="", company="", address="", home="", mobile="", work="", fax="",
                    email="", email2="", email3="", homepage="", byear="", address2="", phone2="", notes="")] + [
    Contact(firstname=random_letters("firstname", 20), middlename=random_letters("", 20), lastname=random_letters("lastname", 20),
            nickname=random_letters("", 20), title=random_letters("", 20), company=random_letters("", 20), address=random_letters("", 20),
            home=random_letters("homephone", 20), mobile=random_letters("", 20), work=random_letters("", 20), fax=random_letters("", 20),
            email=random_letters("email", 20), email2=random_letters("", 20), email3=random_letters("", 20), homepage=random_letters("", 20),
            byear=random_year(4), address2=random_letters("", 20), phone2=random_letters("", 20), notes=random_letters("", 20))
    for i in range(n)] + [
    Contact(firstname=random_string("firstname", 20), middlename=random_string("", 20), lastname=random_string("lastname", 20),
            nickname=random_string("", 20), title=random_string("", 20), company=random_string("", 20), address=random_string("", 20),
            home=random_string("homephone", 20), mobile=random_string("", 20), work=random_string("", 20), fax=random_string("", 20),
            email=random_string("email", 20), email2=random_string("", 20), email3=random_string("", 20), homepage=random_string("", 20),
            byear=random_year(4), address2=random_string("", 20), phone2=random_string("", 20), notes=random_string("", 20))
    for j in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))