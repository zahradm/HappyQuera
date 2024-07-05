sequence_number, k = map(int, input().split())

*sequence, = map(int, input().split())

final = []
res = 0
if len(sequence) == sequence_number:
    for i in range(sequence_number):
        if len(sequence) > 2:
            if sequence[1] - sequence[0] > k:
                final.append(k * (i + 1) + sequence[0])
            else:
                final.append(k * (i - 1) + sequence[0])
            res = sum(abs(x - y) for x, y in zip(final, sequence))
        elif len(sequence) == 2:
            res = abs(sequence[0] - sequence[1] - k)
        else:
            res = abs(sequence[0] - k)

print(res)
