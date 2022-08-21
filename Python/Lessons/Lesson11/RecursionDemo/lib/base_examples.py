def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def power(a: float, n: int) -> float:
    if n == 1:
        return a
    else:
        return a * power(a, n - 1)


def fibo(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
