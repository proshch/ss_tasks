"""This module is for creating test script for catching
different types of exceptions"""


def personal_info(name):
    """Method to creating test data for catching
    different types of exceptions

    Positional argumnet:
    name - string with name
    """
    age_list = [31, 22, 43]
    name_list = ['Alex', 'Lorenzo', 'Fabio']
    info = {name: age for name in name_list for age in age_list}
    print('{} age is {}'.format(name, info[name])) 
    for i in range(0, 3):
        print(age_list[i])
    print(z)
    
 
try:
    personal_info('Alex', 1)
except TypeError:
    print("Type Error is catched!")
except KeyError as key :
    print("Person with this name does not exist: {}".format(key))
except IndexError as index:
    print('Element with that index does not exit: {}'.format(index))
except Exception as e:
    print('Unexpected Error: {}'.format(e))
else:
    print("Ohh..so close to Error..")
finally:
    print("Anyway error can`t stop me!!")


