"""
CS3B Lab 3: Recursion, Search, and Sort
Brandon Cunnane
This program asks the user for a list, then duplicates the entries.
It also searches the values and sorts the list if desired.
"""


def get_list():
    """
    Prompts the user for list entries separated by spaces.
    """
    while True:
        alist = input("Enter elements of a list separated by space: ")
        if alist == '':
            print("Invalid entry. List cannot be empty.")
            continue
        alist = alist.split()
        return alist


def duplicate_elements(alist, duplicated):
    """
    Duplicates each element in the list.
    """
    if len(alist) == 0:
        print(f"Duplicated list: {duplicated}")
        return duplicated
    else:
        duplicated.append(alist[0])
        duplicated.append(alist[0])
        duplicate_elements(alist[1:], duplicated)


def sort_list(alist):
    """
    Sorts the elements in the list.
    """
    alist.sort()
    print(f"Sorted list: {alist}")


def search_list(alist):
    """
    Searches list for the presence of the entered key.
    """
    key = input("Enter search key: ")
    if key in alist:
        print(f"{key} is in the list")
    else:
        print(f"{key} is not in the list")


def main():
    options = [duplicate_elements, sort_list, search_list]
    while True:
        alist = get_list()
        while True:
            print(f"\nlist: {alist}")
            choice = input(("Options:\n"
                            "(1) Duplicate list elements\n"
                            "(2) Sort list\n"
                            "(3) Search list\n"
                            "(4) Enter new list\n"
                            "Enter # for desired option: "))
            if choice == '1':
                duplicate_elements(alist, [])
            elif choice == '2':
                sort_list(alist)
            elif choice == '3':
                search_list(alist)
            elif choice == '4':
                break
            else:
                print("Invalid entry. Enter option #.")


if __name__ == '__main__':
    main()

"""
Enter elements of a list separated by space: 
Invalid entry. List cannot be empty.
Enter elements of a list separated by space: to be or not to be

list: ['to', 'be', 'or', 'not', 'to', 'be']
Options:
(1) Duplicate list elements
(2) Sort list
(3) Search list
(4) Enter new list
Enter # for desired option: 1
Duplicated list: ['to', 'to', 'be', 'be', 'or', 'or', 'not', 'not', 'to', 'to', 'be', 'be']

list: ['to', 'be', 'or', 'not', 'to', 'be']
Options:
(1) Duplicate list elements
(2) Sort list
(3) Search list
(4) Enter new list
Enter # for desired option: 4
Enter elements of a list separated by space: how is your day going

list: ['how', 'is', 'your', 'day', 'going']
Options:
(1) Duplicate list elements
(2) Sort list
(3) Search list
(4) Enter new list
Enter # for desired option: 1
Duplicated list: ['how', 'how', 'is', 'is', 'your', 'your', 'day', 'day', 'going', 'going']

list: ['how', 'is', 'your', 'day', 'going']
Options:
(1) Duplicate list elements
(2) Sort list
(3) Search list
(4) Enter new list
Enter # for desired option: 2
Sorted list: ['day', 'going', 'how', 'is', 'your']

list: ['day', 'going', 'how', 'is', 'your']
Options:
(1) Duplicate list elements
(2) Sort list
(3) Search list
(4) Enter new list
Enter # for desired option: 3
Enter search key: day
day is in the list

list: ['day', 'going', 'how', 'is', 'your']
Options:
(1) Duplicate list elements
(2) Sort list
(3) Search list
(4) Enter new list
Enter # for desired option: 3
Enter search key: abc
abc is not in the list
"""