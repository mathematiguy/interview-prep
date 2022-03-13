# Calculate pi to 6 digits using the following convergent series
#
#  pi/4 = 1 – 1/3 + 1/5 – 1/7 + 1/9 + ...

import math
from time import time


def main():
    tol = 1e-6
    diff = 1
    i = 0
    total = 0
    while diff > tol:
        diff = 1 / (2*i+1)
        if i % 2 == 0:
            total += diff
        else:
            total -= diff
        i += 1

    pi_est = total * 4

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
