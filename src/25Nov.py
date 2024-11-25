
def binary_search(input_arr, target_number):
    low = 0
    high = len(input_arr) - 1
    while low <= high:
        middle_index = (high + low) // 2
        if target_number > input_arr[middle_index]:
            low = middle_index + 1
        elif target_number < input_arr[middle_index]:
            high = middle_index - 1
        else:
            return middle_index
    return None


if __name__ == "__main__":
    print(binary_search([1,2,3,4,5,6,7,8,9,10], 9))