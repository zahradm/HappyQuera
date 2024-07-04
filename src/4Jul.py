input_number = int(input())

divisor = []
if input_number != 0:
    for i in range(1, input_number + 1):
        if input_number%i==0:
            divisor.append(i)
divisor.remove(input_number)
sum_of_divisor = sum(divisor)
if (sum_of_divisor & (sum_of_divisor-1) == 0) and sum_of_divisor != 0:
    print(1)
else:
    print(0)

