from files import write_array_into_file
from random import randint

array = [randint(1,1000) for _ in range(50)]
file_name = f'files/input.txt'

write_array_into_file(file_name=file_name, array=array)
