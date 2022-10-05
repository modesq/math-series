def fibonacci(n: int):
    if n == 0:
        return 0
    elif n in {1, 2}:
        return 1
    elif n > 0:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        negate = n < 1 and (n % 2) == 0
        return -fibonacci(abs(n)) if negate else fibonacci(abs(n))


def lucas_series(n: int):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 0:
        return lucas_series(n - 1) + lucas_series(n - 2)
    else:
        negate = n < 1 and (n % 2) == 0
        return -lucas_series(abs(n)) if negate else lucas_series(abs(n))


def sum_series(n: int, x=0, y=1):
    if x == 0 and y == 1:
        return fibonacci(n)
    elif (x == 1 and y == 2) or (x == 2 and y == 1):
        return lucas_series(n)
    else:
        series = [0] * n
        series[0] = x
        series[1] = y
        for i in range(2, n):
            series[i] = series[i - 1] + series[i - 2]
        return series[n - 1]
