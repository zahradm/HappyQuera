import math
import itertools

input = int(input())

n = math.ceil(math.log2(input + 2))

last_sum = -2 * (1 - 2 ** n)
last_last_sum = -2 * (1 - 2 ** (n - 1))

x = ['a', 'b']
list_of_items = []
if n < 2:
    last_sum = - 2 * (1 - 2 ** (n - 1))
    last_last_sum = -2 * (1 - 2 ** (n - 2)) + 1
if input <= last_last_sum:
    list_of_items = [''.join(p) for p in itertools.product(x, repeat=n - 1)]
elif input > last_last_sum:
    list_of_items = [''.join(p) for p in itertools.product(x, repeat=n)]

index = -2 * (1 - 2 ** (n - 2))

print(list_of_items[input - index - 1][-1])
