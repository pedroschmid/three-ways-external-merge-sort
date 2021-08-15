from flags import default_flags
from files import open_array_file, write_array_into_file
from sorts import merge_sort

def main():
    file_name = default_flags() # Getting file_name from flags passed to script vi CLI

    array = open_array_file(file_name=file_name)

    # 3 registry internal memory 
    tape_list = [[], [], []] 

    for index, value in enumerate(array):
        tape_index = int(index / 6) % 3
        tape_list[tape_index].append(value)

        # writing input tape files
        if int(index / 6) % 3 == 0:
            file_name = f'files/input_tape0.txt'
        elif int(index / 6) % 3 == 1:
            file_name = f'files/input_tape1.txt'
        elif int(index / 6) % 3 == 2:
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

if __name__ == '__main__':
    main()
