"""
CS3A  - Assignment 9, Contact list, part 1
Brandon Cunnane
Note: uses starter code
"""


class Sorter:
    """
    This is the bubble sort presented in lectures, the only difference is
    that the two functions are now static methods of a class.
    """

    # TODO part 2: change whatever's necessary to sort by first/last name

    @staticmethod
    def float_largest_to_top(lst, size):
        swapped = False
        for i in range(size - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        return swapped

    @staticmethod
    def sort(lst, by):
        size = len(lst)
        while Sorter.float_largest_to_top(lst, size):
            size -= 1


class Contact:
    """
    This class represents a single contact (one person)
    """
    def __init__(self, first_name, last_name, email=None, phone=None):
        """
        This is the initializer for Contact class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    # setter and getter
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
        if not (type(email) is str or email is None):
            raise TypeError("Invalid email, should be str or None")
        if type(email) is str:
            if "@" not in email:
                raise ValueError("Email must contain '@' character")
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if not (type(phone) is str or phone is None):
            raise TypeError("Invalid phone, should be str or None")
        if type(phone) is str:
            if int(phone) <= 0:
                raise ValueError("Phone must be a positive integer")
        self._phone = phone

    def __str__(self):
        """
        Return a str that that shows all contact info
        """
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Email: {self.email}\n"
                f"Phone: {self.phone}\n")


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

        # TODO part 2: add any necessary code to help search by first/last name

    def clear(self):
        """
        Clear/remove all contacts
        :return:
        """
        self._contacts.clear()

        # TODO part 2: add any necessary code to clear all contacts

    @property
    def contacts(self):
        return self._contacts

    def add(self, contact):
        """
        Add a single contact (one person) to the internal data structures
        raise TypeError if contact is not an instance of class Contact
        """
        if type(contact) is not Contact:
            raise TypeError("Invalid contact entry. Must be Contact type")
        self._contacts.append(contact)

        # TODO part 2: add necessary code to enable search by first/last name

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

    def __str__(self, by=BY_FIRST_NAME):
        """
        Return a str that contains all contact, sorted by first names or
        last name, depending on the "by" parameter.
        It raises a ValueError if the "by" parameter contains invalid value.
        """
        string = ''
        return ''.join([string + str(_) + '\n' for _ in self.contacts])


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
        first_name,last_name[,email][,phone]
    to an instance of Contact
    :param line: the line to convert from
    :return: An instance of Contact
    :raise exception if the line doesn't have at least two comma-separated
           fields, or if any of the fields are invalid.
    """
    values = line.replace(' ', '').replace('\n', '').split(',')
    num_values = len(values)
    if num_values == 2:
        contact = Contact(values[0], values[1])
    elif num_values == 3:
        contact = Contact(values[0], values[1], values[2])
    elif num_values == 4:
        contact = Contact(values[0], values[1], values[2], values[3])
    else:
        raise ValueError("Invalid number of items")
    return contact


def load_contacts_from_file(contact_list, filename):
    """
    Add all contacts contained in the file specified by filename to contact_list
    :param contact_list: instance of ContactList; new contacts should be added to it
    :param filename: name of file to read contacts from
    :return: None
    """
    with open(filename) as f:
        for line in f:
            contact_list.add(line_to_contact(line))


def load_contacts(contact_list):
    """
    Prompts the user for the name of a file, and load contact from that file.
    """
    filename = input("Enter the name of the file to load: ")
    contact_list.clear()

    # print it out.
    try:
        load_contacts_from_file(contact_list, filename)
        print("Loaded {} contacts from {}".format(len(contact_list.contacts),
                                                  filename))
    except Exception as e:
        print(f"Problem loading contacts: {e}")


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


def test_classes():
    c1 = Contact("Frank", "Vogel")
    c2 = Contact("LeBron", "James", "lbj@lakers.com")
    c3 = Contact("Anthony", "Davis", "ad@lakers.com", "2138763091")
    c4 = Contact("Alex", "Caruso", email="ac@lakers.com")
    c5 = Contact("Kyle", "Kuzma", phone="2138490245")
    print(str(c3))

    lakers = ContactList()
    lakers.add(c1)
    lakers.add(c2)
    lakers.add(c3)
    lakers.add(c4)
    lakers.add(c5)
    print(str(lakers))


def test_global_functions():
    # test line_to_contact()
    contacts = (["Frank, Vogel",
                 "LeBron, James, lbj@lakers.com",
                 "Anthony, Davis, ad@lakers.com, 2138763091",
                 ",C",
                 "B,",
                 "B",
                 "B,C,bc@gmail.com,1234567890,1234567890",
                 "B,C,bcgmail.com",
                 "B,C,bc@gmail.com,-1234567890"])
    for contact in contacts:
        try:
            print(str(line_to_contact(contact)))
        except Exception as e:
            print(f"Error: {e}")

    # test load_contacts_from_file()
    contact_list = ContactList()
    try:
        load_contacts_from_file(contact_list, 'badfilename')
    except Exception as e:
        print(f"Error: {e}")

    # load_contacts(contact_list)
    # print(contact_list)


def main():
    contact_list = ContactList()

    while True:
        choice = get_choice()

        if choice == 1:
            load_contacts(contact_list)
        elif choice == 2:
            print_by_first_name(contact_list)
        elif choice == 3:
            print_by_last_name(contact_list)
        elif choice == 4:
            find_by_first_name(contact_list)
        elif choice == 5:
            find_by_last_name(contact_list)
        elif choice == 6:
            quit(contact_list)
        else:
            print("Invalid choice")


if __name__ == '__main__':
    print('*** TESTING ***')
    test_classes()
    test_global_functions()
    print('*** MAIN ***')
    main()
