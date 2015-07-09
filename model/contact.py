# -*- coding: utf-8 -*-

from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None, byear=None,
                 address2=None, phone2=None, notes=None, id=None, all_emails_from_home_page=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.home, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and (self.lastname == other.lastname)\
               and (self.firstname == other.firstname)\
               and (self.address == other.address)\
               and (self.all_emails_from_home_page == other.all_emails_from_home_page)\
               and (self.all_phones_from_home_page == other.all_phones_from_home_page)

    # Более информационный __eq__!!!
    def __eq1__(self, other):
        if not (self.id is None or other.id is None or self.id == other.id):
            print("ID не равны")
            return False
        if self.lastname != other.lastname:
            print(self.lastname + "!=" + other.lastname)
            return False
        if self.firstname != other.firstname:
            print(self.firstname + "!=" + other.firstname)
            return False
        if self.address != other.address:
            print(self.address + "!=" + other.address)
            return False
        if self.all_emails_from_home_page != other.all_emails_from_home_page:
            print(self.all_emails_from_home_page + "!=" + other.all_emails_from_home_page)
            return False
        if self.all_phones_from_home_page != other.all_phones_from_home_page:
            print(self.all_phones_from_home_page + "!=" + other.all_phones_from_home_page)
            return False
        return True

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize