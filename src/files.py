from parses import to_number
from logs import print_success, print_error
from json import dumps

def open_array_file(file_name):
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            print_success(f'Opened {file_name} successfully')
            return [to_number(string=f.rstrip()) for f in file]
    except IOError:
        print_error(f'Could not open {file_name}')
        exit()

def write_array_into_file(file_name, array):
    try:
        with open(file_name, mode='wt', encoding='utf-8') as file:
            print_success(f'Writing {array} into {file_name}')
            file.write('\n'.join(str(item) for item in array))
    except IOError:
        print_error(f'Could not open {file_name}')
        exit()

def write_dictionary_into_file(file_name, array_of_dictionary):
    try:
        with open(file_name, mode='wt', encoding='utf-8') as file:
            print_success(f'Writing {array_of_dictionary} into {file_name}')
            file.write(',\n'.join(dumps(dictionary) for dictionary in array_of_dictionary))
    except IOError:
        print_error(f'Could not open {file_name}')
        exit()