import time
from main import services


def get_service1():
    while True:
        try:
            s1 = str(input('Select first service: '))
            s1 = s1.capitalize()

            if s1 not in services:
                raise ValueError('Invalid service.')
            else:
                break

        except ValueError as e:
            print(e)
            print('Please try again.\n')

    return s1


def get_service2():
    while True:
        try:
            s2 = str(input('Select second service: '))
            s2 = s2.capitalize()

            if s2 not in services:
                raise ValueError('Invalid service.')
            else:
                break

        except ValueError as e:
            print(e)
            print('Error. Please try again.\n')

    return s2
