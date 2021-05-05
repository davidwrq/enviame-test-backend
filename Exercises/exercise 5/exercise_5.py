from functools import reduce


def factors(number):
    """
    Calculate how many divisor has the number given
    Args:
        number (int): fibonnaci number

    Returns:
        [tuple]: with divisors values
    """
    return set(
        reduce(
            list.__add__,
            ([i, number // i] for i in range(1, int(number ** 0.5) + 1) if number % i == 0),
        )
    )


def fib_counter_divisor():
    """
    functions that find first fib number with more than 1000 divisors.

    Returns:
        [String]: first fib number with more than 1000 divisors.
    """
    sum = 1
    i = 0
    j = 1
    # check if we have more than 1000 divisors
    while len(list(factors(sum))) < 1000:
        sum = i + j
        i = j
        j = sum
    return f"primer número de Fibonacci que tiene más de 1000 divisores: {sum}"


print(fib_counter_divisor())
