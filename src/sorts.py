def merge_sort(array):
    if len(array) > 1:
        left_array = array[:len(array) // 2]
        right_array = array[len(array) // 2:]

        merge_sort(left_array)
        merge_sort(right_array)

        left_array_element = 0
        right_array_element = 0
        merged_array_element = 0
        
        while left_array_element < len(left_array) and right_array_element < len(right_array):
            if left_array[left_array_element] < right_array[right_array_element]:
                array[merged_array_element] = left_array[left_array_element]
                left_array_element += 1

            else:
                array[merged_array_element] = right_array[right_array_element]
                right_array_element += 1

            merged_array_element += 1

        while left_array_element < len(left_array):
            array[merged_array_element] = left_array[left_array_element]

            left_array_element += 1
            merged_array_element += 1

        while right_array_element < len(right_array):
            array[merged_array_element] = right_array[right_array_element]

            right_array_element += 1
            merged_array_element += 1