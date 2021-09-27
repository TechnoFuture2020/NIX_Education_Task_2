# - - - - NIX - - - - -
"""
TASK_2:
Напишите template строки, который можно будет многократно переиспользовать,
вставляя в него имя и фамилию человека.
"""


def get_name_surname_user():
    name_user = input('Enter your name: ')
    surname_user = input('Enter your surname: ')
    template = 'My name is {0}. My surname is {1}'.format(name_user, surname_user)
    return template


print(get_name_surname_user())
