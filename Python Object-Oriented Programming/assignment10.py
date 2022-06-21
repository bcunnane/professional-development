"""
CS 3A  - Lab Assignment 10, Contact list, Part 2
Brandon Cunnane
Note: started from assignment 9 instructor solution

EXTRA CREDIT: this code includes the main() extra credit
"""


class Sorter:
    """
    This is the bubble sort presented in lectures, the only difference is
    that the two functions are now static methods of a class.
    """

    # TODO part 2: change whatever's necessary to sort by first/last name

    @staticmethod
    def float_largest_to_top(lst, size, by):
        swapped = False
        for i in range(size - 1):
            if by == lst.BY_FIRST_NAME:
                names = []
                [names.append(n.first_name) for n in lst.contacts]
                name_dict = lst._first_name_dict
            elif by == lst.BY_LAST_NAME:
                names = []
                [names.append(n.last_name) for n in lst.contacts]
                name_dict = lst._last_name_dict
            else:
                raise ValueError("Input by must be BY_FIRST_NAME or BY_LAST_NAME")
            if names[i] > names[i + 1]:
                lst.contacts[i], lst.contacts[i + 1] = lst.find(names[i + 1], by), lst.find(names[i], by)
                swapped = True
        return swapped

    @staticmethod
    def sort(lst, by):
        size = len(lst.contacts)
        while Sorter.float_largest_to_top(lst, size, by):
            size -= 1


class Contact:
    """
    This class represents a single contact (one person)
    """

    # Part 1: make email and phone optional parameters that default to None
    def __init__(self, first_name, last_name, email=None, phone=None):
        """
        This is the initializer for Contact class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def __str__(self):
        """
        Return a str that that shows all contact info
        """
        # Part 1: return a str that contains all 4 attributes
        # String preceded by f is called f-string, and is a more readable
        # way of incorporating information into a string than str.format()
        return (f"Name:  {self.first_name} {self.last_name}\n"
                f"Email: {self.email}\n"
                f"Phone: {self.phone}\n")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if type(first_name) != str:
            raise TypeError("Invalid first name, should be str")
        if len(first_name) == 0:
            raise ValueError("First name cannot be empty")
        self._first_name = first_name

    # TODO part 1: turn other attributes into properties with "Pythonic"
    # setter and getter
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if type(last_name) != str:
            raise TypeError("Invalid last name, should be str")
        if len(last_name) == 0:
            raise ValueError("Last name cannot be empty")
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if email is not None:
            if type(email) != str:
                raise TypeError("Invalid type for email")
            if "@" not in email:
                raise ValueError("Invalid email")
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if phone is not None:
            if type(phone) != str:
                raise TypeError("Invalid type for phone")
            # Make sure it's an positive int; if it's not
            # an int, int(phone) will raise an exception.
            if int(phone) <= 0:
                raise ValueError("Phone number cannot be negative")
        self._phone = phone


class ContactList:
    """
    This class stores multiple contacts.
    """
    BY_FIRST_NAME = 1  # sort/find by first name
    BY_LAST_NAME = 2  # sort/find by last name

    def __init__(self):
        """
        Creates a list of contacts, and also dict's that associated contacts with
        first names and last names
        """
        self._contacts = []
        self._first_name_dict = {}
        self._last_name_dict = {}

        # TODO part 2: add any necessary code to help search by first/last name

    def clear(self):
        """
        Clear/remove all contacts
        """
        self._contacts.clear()
        self._first_name_dict.clear()
        self._last_name_dict.clear()

        # TODO part 2: add any necessary code to clear all contacts

    @property
    def contacts(self):
        return self._contacts

    def add(self, contact):
        """
        Add a single contact (one person) to the interal data structures
        raise TypeError if contact is not an instance of class Contact
        """
        # Part 1: add contact to list of contacts
        if type(contact) != Contact:
            raise TypeError(f"Type is {type(contact).__class__.__name__}, not Contact")

        self._contacts.append(contact)
        self._first_name_dict[contact.first_name] = contact
        self._last_name_dict[contact.last_name] = contact

        # TODO part 2: add any necessary code to enable search by first/last name

    def find(self, name, by):
        """
        Find a contact by the given name
        :param name: the first/last name of the contact to lookup, depend on by
        :param by: if BY_FIRST_NAME, name should be interpreted as the first name
                   if BY_LAST_NAME, name should be interpreted as the last name
        :return: an instance of Contact, the first_name/last_name attribute of which
                 matches name; if no match, returns None
        """
        # TODO part 2: add any necessary code to enable search by first/last name

        if by != ContactList.BY_FIRST_NAME and by != ContactList.BY_LAST_NAME:
            raise ValueError("Input by must be BY_FIRST_NAME or BY_LAST_NAME")

        if by == ContactList.BY_FIRST_NAME:
            try:
                return self._first_name_dict[name]
            except:
                return None
        elif by == ContactList.BY_LAST_NAME:
            try:
                return self._last_name_dict[name]
            except:
                return None

    def __str__(self, by=BY_FIRST_NAME):
        """
        Return a str that contains all contact, sorted by first names or
        last name, depending on the "by" parameter.
        It raises a ValueError if the "by" parameter contains invalid value.
        """
        # Part 1, return a string that contains all contacts in the list
        if by != ContactList.BY_FIRST_NAME and by != ContactList.BY_LAST_NAME:
            raise ValueError("Input by must be BY_FIRST_NAME or BY_LAST_NAME")

        Sorter.sort(self, by)
        return "\n".join([str(c) for c in self._contacts])
        # TODO part 2: add any necessary code to handle sorting by first/last name


def get_choice():
    """
    Repeatedly prompts the user for an integer until they do so.
    :return: An integer choice.
    """
    while True:
        try:
            choice = int(input(
                "\n"
                "****** Contact List ******\n"
                "Please choose from the following actions:\n"
                "  1. Load contacts from file\n"
                "  2. Print all contacts, sorted by first name\n"
                "  3. Print all contacts, sorted by last name\n"
                "  4. Search all contacts by first name\n"
                "  5. Search all contact by last name\n"
                "  6. Quit\n"
                "Please enter your choice: "))
            return choice
        except:
            print("Invalid input")


def line_to_contact(line):
    """
    Convert a line of str of the form
        "first_name, last_name [, email] [, phone]"
    to an instance of Contact
    :param line: the line to convert from
    :return: An instance of Contact
    :raise exception if the line doesn't have at least two comma-separated
           fields, or if the email or phone number is invalid
    """
    # Part 1: convert a line of str to an instance of Contact

    fields = [f.strip() for f in line.split(",")]
    # If len(fields) is less than 2, the following will raise IndexError
    # exception, which satisfies the requirement to raise any exception.
    contact = Contact(fields[0], fields[1])

    # If email or phone is incorrect, the setter will raise exception, and
    # we'll allow the exception to propagate up to the caller
    if len(fields) > 2:
        contact.email = fields[2]
    if len(fields) > 3:
        contact.phone = fields[3]

    return contact


def load_contacts_from_file(contact_list, filename):
    """
    Add all contacts contained in the file specified by filename to contacts
    :param contact_list: instance of ContactList; new contacts should be added to it
    :param filename: name of file to read contacts from
    :return: None
    """
    # Part 1: add all contacts from file to contact list
    with open(filename) as f:
        for line in f:
            try:
                contact = line_to_contact(line)
                contact_list.add(contact)
            except:
                # Any exception, we skip the line/contact
                # When debugging, may consider printing out e, i.e.
                # print(f"Line '{line}' causes exception: {e}")
                pass


def load_contacts(contact_list):
    """
    Prompts the user for the name of a file, and load contact from that file.
    """
    filename = input("Enter the name of the file to load: ")
    contact_list.clear()

    # Part 1: handle any exception raised by load_contacts_from_file() and
    # print it out.
    try:
        load_contacts_from_file(contact_list, filename)
        print("Loaded {} contacts from {}".format(len(contact_list.contacts), filename))
    except Exception as e:
        print("Problem loading contacts: {}".format(e))


def print_by_first_name(contact_list):
    print("\n" + contact_list.__str__(ContactList.BY_FIRST_NAME))


def print_by_last_name(contact_list):
    print("\n" + contact_list.__str__(ContactList.BY_LAST_NAME))


def find_contact(contact_list, by):
    name = input("Please enter the name to search: ")
    contact = contact_list.find(name, by)
    print("\n" + str(contact))


def find_by_first_name(contact_list):
    find_contact(contact_list, ContactList.BY_FIRST_NAME)


def find_by_last_name(contact_list):
    find_contact(contact_list, ContactList.BY_LAST_NAME)


def quit(contact_list):
    """
    Do cleanup and exit program; ok to use exit() in this function in this assignment.
    :param contact_list:
    :return: (Never, because it exits the program)
    """
    print("Bye!")
    exit(0)


def test():
    c1 = Contact("Frank", "Vogel")
    c2 = Contact("LeBron", "James", "lbj@lakers.com")
    c3 = Contact("Anthony", "Davis", "ad@lakers.com", "2138763091")
    c4 = Contact("Alex", "Caruso", email="ac@lakers.com")
    c5 = Contact("Kyle", "Kuzma", phone="2138490245")

    lakers = ContactList()
    lakers.add(c1)
    lakers.add(c2)
    lakers.add(c3)
    lakers.add(c4)
    lakers.add(c5)

    print(ContactList.__str__(lakers, ContactList.BY_LAST_NAME))


def main():
    contact_list = ContactList()
    funcs = [load_contacts,
             print_by_first_name,
             print_by_last_name,
             find_by_first_name,
             find_by_last_name,
             quit]
    while True:
        choice = get_choice()
        funcs[choice - 1](contact_list)


if __name__ == '__main__':
    # test()
    main()
