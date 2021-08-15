from flags import default_flags
from files import open_array_file, write_array_into_file, write_dictionary_into_file
from logs import print_result
from sorts import merge_sort

def main():
    # Getting file_name from flags passed to script vi CLI
    file_name = default_flags() 

    # Initializing array variable with file values
    array = open_array_file(file_name=file_name)

    # 3 registry internal memory 
    tape_list = [[], [], []] 

    # aux data structure to save element and tape
    array_of_dictionary = []

    for index, value in enumerate(array):
        tape_index = int(index / 6) % 3
        tape_list[tape_index].append(value)

        # writing input tape files
        if int(index / 6) % 3 == 0:
            array_of_dictionary.append({ 'tape': 'input_tape0', 'element': value})
            file_name = f'files/input_tape0.txt'
        elif int(index / 6) % 3 == 1:
            array_of_dictionary.append({ 'tape': 'input_tape1', 'element': value})
            file_name = f'files/input_tape1.txt'
        elif int(index / 6) % 3 == 2:
            array_of_dictionary.append({ 'tape': 'input_tape2', 'element': value})
            file_name = f'files/input_tape2.txt'

        array = tape_list[tape_index]
        write_array_into_file(file_name=file_name, array=array)

    # output tape files
    for index, tape in enumerate(tape_list):
        merge_sort(tape)

        file_name = f'files/output_tape{index}.txt'
        write_array_into_file(file_name=file_name, array=tape)

    # writing sorted merged_tapes into output file
    merged_tapes = [item for sub_tapelist in tape_list for item in sub_tapelist]

    merge_sort(merged_tapes)

    write_array_into_file(file_name='files/output.txt', array=merged_tapes)
    write_dictionary_into_file(file_name='files/dictionary.txt', array_of_dictionary=array_of_dictionary)

if __name__ == '__main__':
    main()
