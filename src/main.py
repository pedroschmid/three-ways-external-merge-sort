from flags import default_flags
from logs import print_result
from files import open_array_file, write_array_into_file
from sorts import merge_sort
from load_balancing import three_ways_load_balancing

def main():
    file_name = default_flags() # Getting file_name from flags passed to script vi CLI

    array = open_array_file(file_name=file_name)
    
    three_ways_load_balancing(array=array)

if __name__ == '__main__':
    main()
