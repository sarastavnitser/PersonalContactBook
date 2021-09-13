

class ContactItem:  # ContactItem
    lastName, firstName, email, homephone = '', '', '', ''

    def __init__(self, last, first, mail, number1):  # constructor
        self.lastName = last.strip().capitalize()
        self.firstName = first.strip().capitalize()
        self.email = mail.strip().lower()
        self.homephone = number1



    def __str__(self):
        s = '{:12s}, {:10s}, {:>30s}, {:>12s},'
        return s.format(self.lastName, self.firstName, self.email, self.homephone)


class ContactBook:
    owner = ''
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


    def __init__(self, name):
        self.owner = name.strip().capitalize()
        self.contact_list = []

    def __eq__(self, other):
        if self.lastName.lower() == other.lastName.lower() and \
                self.firstName.lower() == other.firstName.lower():
            return True

        else:
            return False

    def addNewContact(self, last_name, first_name, newMail, newPhone):
        if newPhone.strip() == '':
            newPhone = ''
        else:
            if len(newPhone.strip()) != 12 or newPhone.strip()[3] != '-' or newPhone.strip()[7] != '-':
                print("Invalid Phone Number")
                newPhone = ''
            elif newPhone[0] not in self.numbers or  newPhone[1] not in self.numbers or  newPhone[2] not in\
                self.numbers or  newPhone[4] not in self.numbers or  newPhone[5] not in self.numbers or \
                newPhone[6] not in self.numbers or  newPhone[8] not in self.numbers or  newPhone[9] not in \
                self.numbers or  newPhone[10] not in self.numbers or  newPhone[11] not in self.numbers:
                print("Invalid Phone Number")
                newPhone = ''
        if newMail.strip() == '':
            newMail = ''
        else:
            newMail = newMail.strip().lower()
            end = newMail.strip()[-4:-1], newMail.strip()[-1]
            acceptableEnds = ['.com', '.edu', '.gov', '.net']
            if '@' not in newMail or ''.join(end) not in acceptableEnds or newMail.strip()[0] == '@' or \
                    newMail.count('@') > 1 or (newMail.strip()[-5] == "@" and newMail.strip()[-4] == "."):
                print("Invalid Email Address")
                newMail = ''

        contact = ContactItem(last_name, first_name, newMail, newPhone)
        self.contact_list.append(contact)
        self.contact_list.sort(key=lambda x: (x.lastName, x.firstName, x.email, x.homephone))
        return

    def updateContact(self, lastName, firstName, newLast, newFirst, newMail, newPhone):
        for contact in self.contact_list:
            if lastName.strip().capitalize() == contact.lastName:
                if firstName.strip().capitalize() == contact.firstName:
                    if newLast.strip() == '':
                        continue
                    else:
                        contact.lastName = newLast.strip().capitalize()
                    if newFirst.strip() ==  '':
                        continue
                    else:
                        contact.firstName = newFirst.strip().capitalize()
                    if newMail.strip() == '':
                        continue
                    else:
                        end = newMail.strip()[-4:-1], newMail.strip()[-1]
                        acceptableEnds = ['.com', '.edu', '.gov', '.net']
                        if '@' not in newMail or ''.join(end) not in acceptableEnds or newMail.strip()[0] == '@' or \
                                newMail.count('@') > 1 or (newMail.strip()[-5] == "@" and newMail.strip()[-4] == "."):
                            print("Invalid Email Address")
                            return
                        else:
                            contact.email = newMail.strip().capitalize()
                    if newPhone.strip() == '':
                        continue
                    else:
                        if len(newPhone.strip()) != 12 or newPhone.strip[3] != '-' or newPhone.strip()[7] != '-':
                            print("Invalid Phone Number")
                            return
                        elif newPhone[0] not in self.numbers or  newPhone[1] not in self.numbers or  newPhone[2] not in\
                            self.numbers or  newPhone[4] not in self.numbers or  newPhone[5] not in self.numbers or \
                            newPhone[6] not in self.numbers or  newPhone[8] not in self.numbers or  newPhone[9] not in \
                            self.numbers or  newPhone[10] not in self.numbers or  newPhone[11] not in self.numbers or \
                            newPhone[12] not in self.numbers:
                            print("Invalid Phone Number")
                            return
                        else:
                            contact.phone = newPhone.strip()
                else:
                    continue
            else:
                continue
        print('Contact not found')
        print()


    def removeContact(self, lastName, firstName):
        for contact in self.contact_list:
            if lastName.strip().capitalize() == contact.lastName:
                if firstName.strip().capitalize() == contact.firstName:
                    self.contact_list.remove(contact)

    def locateContact(self, lastName, firstName):
        for contact in self.contact_list:
            if lastName.strip().capitalize() == contact.lastName:
                if firstName.strip().capitalize() == contact.firstName:
                    print(contact)
                    print()

    def display(self):
        if len(self.contact_list) == 0:
            print('sorry, no contacts found')
            print()
            return
        print(self.owner, '\'s contacts:', sep='')
        for contact in self.contact_list:
            print(contact)
        print()
        return


a = ContactBook(" aaron ")
b = ContactBook(" BETH ")

a.addNewContact(" smith", " alice ", "asm@aol.net", "111-222-3333")
a.addNewContact(" smith", " martha ", "mas@gmail.com", "212-666-1122")
a.addNewContact(" berk ", " DAVID ", "db@us.gov", "777-666-6622")

b.addNewContact(" jones ", " BOB ", "bj@mit.edu", "203-123-5432")
b.addNewContact(" BAKER ", " BOB ", "bbak@us.gov", "212-555-1212")

a.display()
b.display()