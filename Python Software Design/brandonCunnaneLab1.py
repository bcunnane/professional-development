"""
CS3B Lab 1
Brandon Cunnane
This script asks the user for family name and student ID and performs
calculations based on that input.
"""

import datetime


def get_inputs():
    """
    Obtains user input for family name and student ID.
    Determines my_id (sum of student ID numbers) & n_let (family name length)
    :return: my_id, n_let
    """
    # get user inputs
    family_name = input("Enter your family name: ")
    student_id = input("Enter your student ID: ")

    # calculate values
    my_id = sum([int(i) for i in list(student_id)])
    n_let = len(family_name)

    # validate inputs
    if not (2 <= n_let <= 15):
        raise ValueError("Family name must be between 2 and 15 characters.")
    if not (len(student_id) == 8):
        raise ValueError("Student ID must be 8 characters long.")
    if my_id < 0:
        raise ValueError("Sum of Student ID must be greater than zero.")

    return my_id, n_let


def calc_expressions(my_id, n_let):
    """
    Performs specified expressions on my_id and n_let
    :return: results list
    """
    results = [my_id / 2,
               my_id % 2,
               sum(range(2, n_let + 1)),
               my_id + n_let,
               abs(n_let - my_id),
               my_id / (n_let + 1100),
               (n_let % n_let) and (my_id * my_id),
               1 or (my_id / 0),
               round(3.15, 1)]
    return results


def display(my_id, n_let, results):
    """
    prints inputs and calculations
    """
    # print inputs
    print(f"my_id is: {my_id}")
    print(f"n_let is: {n_let}")

    # print results
    expression_num = 1
    for result in results:
        if type(result) is float:
            result_str = f"{result:.2f}"
        else:
            result_str = str(result)
        print(f"expression {expression_num}: {result_str}")
        expression_num += 1

    # print date
    today = datetime.datetime.now()
    today = today.strftime("%x")
    print(f"Today's date is {today}")


def main():
    my_id, n_let = get_inputs()
    results = calc_expressions(my_id, n_let)
    display(my_id, n_let, results)


if __name__ == '__main__':
    main()

"""
Enter your family name: Cunnane
Enter your student ID: 20160283
my_id is: 22
n_let is: 7
expression 1: 11.00
expression 2: 0
expression 3: 27
expression 4: 29
expression 5: 15
expression 6: 0.02
expression 7: 0
expression 8: 1
expression 9: 3.10
Today's date is 07/04/21
"""