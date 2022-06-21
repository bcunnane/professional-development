'''
CS3A, Assignment #2, Arithmetic
Brandon Cunnane ID 20160283
Submitted April 12, 2021
'''

num_letters = 7
my_id = 20160283

print('My family name is Cunnane')
print('My Student ID is ' + str(my_id))
print('The number of characters in my last name is ' + str(num_letters) + '\n')

result = my_id % 17
print('Expression #1 ------------ : ' + str(result) + '\n')

result = (num_letters + 17) % 11
print('Expression #2 ------------ : ' + str(result) + '\n')

result = my_id / (num_letters + 800)
print('Expression #3 ------------ : ' + str(result) + '\n')

result = 1 + 2 + 3 + 4 + 5 + 6 + num_letters
print('Expression #4 ------------ : ' + str(result) + '\n')

result = 15000 / (80 + (my_id - 123456) / ((num_letters + 20) ** 2))
print('Expression #5 ------------ : ' + str(result))

'''
My family name is Cunnane
My Student ID is 20160283
The number of characters in my last name is 7

Expression #1 ------------ : 0

Expression #2 ------------ : 2

Expression #3 ------------ : 24981.763320941758

Expression #4 ------------ : 28

Expression #5 ------------ : 0.5441612345508097

Process finished with exit code 0
'''