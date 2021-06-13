import math

import sp as sp


def driver():
    x = sp.symbols('x')
    f = (2 * x * math.exp(-x) + math.ln(2 * x ** 2)) * (2 * x ** 2 - 3 * x - 5)
    start = 0
    end = 3


driver()