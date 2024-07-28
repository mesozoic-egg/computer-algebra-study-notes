# ALGORITHM 3.3 at Page 87 of the book

# Recall that the assumption is that the hardware allows us to perform
# Addition, multiplication, and division (Page 84).

# I'll use a list to store the number. Each element within the list can
# be manipulated directly with python's +, -, *, / arithmetic operators.
# And the actual number in decimal can be computed following the
# method presented in "Calculating the value" section of 01.md notes.

from typing import List

def multiply(b: int, u: List[int], v: List[int]) -> List[int]:
    m = len(u)  # u is an m-digit number
    n = len(v)  # v is an n-digit number
    w = [0] * (m + n)
    u = u[::-1]
    v = v[::-1]
    for j in range(m):
        if v[j] == 0:
            continue
        k = 0
        for i in range(n):
            t = u[i] * v[j] + k + w[i + j]
            w[i + j] = t % b
            k = t // b
        w[m + j] = k

    while w[-1] == 0:
        w.pop()
    return w[::-1]


# We can verify this with a decimal example, suppose 12 * 12
assert multiply(10, [1, 2], [1, 2]) == [1, 4, 4]

# Verify that carry works
assert multiply(10, [9, 9], [9, 9]) == [9, 8, 0, 1]
