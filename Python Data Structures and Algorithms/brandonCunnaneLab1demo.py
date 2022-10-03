
from brandonCunnaneLab1 import Movie

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
        
    