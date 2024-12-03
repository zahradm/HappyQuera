

def bubble_sort(input_list: list[int]) -> list[int]:
    while True:
        flag = False
        for i in range(len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                flag = True
        if not flag:
            return input_list


if __name__ == '__main__':
    print(bubble_sort([5, 1, 2, 4, 1]))


