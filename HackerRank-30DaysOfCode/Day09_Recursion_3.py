#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def factorial(n):
    value = 1
    for i in range(n, 0, -1):    # range(start, stop, step) when stop comes loops stops and stop is not reached
        value *= i
    return value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# sample input:
# 3