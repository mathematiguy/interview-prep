# Calculate pi to 12 digits using the following convergent series
#
#  pi/2 = sum( (2n)!! / (2n + 1)!! * (0.5) ** n )
#
# Where !! is the double factorial defined by 0!! = 1!! = 1 and
# n!! = n(n - 2)!!

import math
from time import time
from functools import lru_cache


@lru_cache(1000)
def double_factorial(n):
    assert n >= 0
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * double_factorial(n - 2)


def main():
    tol = 1e-12
    diff = 1

    i = 0
    total = 0
    while diff > tol:
        diff = double_factorial(2 * i) / double_factorial(2 * i + 1) * (0.5) ** i
        total += diff
        i += 1

    pi_est = total * 2

    return i, pi_est


if __name__ == "__main__":

    start = time()
    i, pi_est = main()
    fin = time()

    print(f"Time taken     = {(fin - start) * 1000:.1f} microseconds")
    print(f"Steps required = {i + 1}")
    print(f"True Pi        = {math.pi}")
    print(f"Estimated Pi   = {pi_est}")
    print(f"Relative error = {1 - pi_est / math.pi}")
