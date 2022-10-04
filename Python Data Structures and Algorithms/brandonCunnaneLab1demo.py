"""
Operates a menu for user interaction with the Movie class
"""

from brandonCunnaneLab1 import Movie

def main():
    menu = """COMMAND MENU
    list - List all movies
    add -  Add a movie
    del -  Delete a movie
    exit - Exit program
    """
    print(menu)
    while True:
        command = input("Command: ")
        if command == 'exit':
            print('Bye!')
            break
        elif command == 'list':
            Movie.getList()
        elif command == 'add':
            name = input('Name: ')
            year = int(input('Year: '))
            Movie.add(Movie(name, year))
        elif command == 'del':
            movie_num = int(input('Number: '))
            Movie.delete(movie_num)
        else:
            print('Invalid command.\n')


if __name__ == '__main__':
    main()


"""
COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: add
Name: Ladybird
Year: 2018
Ladybird was added.

Command: add
Name: Call me by your name
Year: 2017
Call me by your name was added.

Command: add
Name: In the Heights
Year: 2021
In the Heights was added.

Command: add
Name: Dune
Year: 2021
Dune was added.

Command: add
Name: The Batman
Year: 2022
The Batman was added.

Command: list
1. Ladybird (2018)
2. Call me by your name (2017)
3. In the Heights (2021)
4. Dune (2021)
5. The Batman (2022)

Command: add
Name: Little Miss Sunshine
Year: 2007
Little Miss Sunshine was added.

Command: list
1. Ladybird (2018)
2. Call me by your name (2017)
3. In the Heights (2021)
4. Dune (2021)
5. The Batman (2022)
6. Little Miss Sunshine (2007)

Command: del
Number: 3
In the Heights was deleted.

Command: list
1. Ladybird (2018)
2. Call me by your name (2017)
3. Dune (2021)
4. The Batman (2022)
5. Little Miss Sunshine (2007)

Command: abc
Invalid command.

Command: exit
Bye!
"""