def multiply_strings(x: str, y: str) -> str:
    x, y = x[::-1], y[::-1]
    res = [0] * (len(x) + len(y))

    for i, d1 in enumerate(x):
        for j, d2 in enumerate(y):
            res[i + j] += int(d1) * int(d2)
            res[i + j + 1] += res[i + j] // 10
            res[i + j] %= 10

    while len(res) > 1 and res[-1] == 0:
        res.pop()

    return ''.join(map(str, res[::-1]))

with open("input.txt") as f:
    a, b = f.readline().split()
    print(multiply_strings(a, b))
