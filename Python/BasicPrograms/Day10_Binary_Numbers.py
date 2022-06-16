#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


if __name__ == '__main__':
    n = int(input().strip())

value = bin(n)
counter = 0
bin_value = value[2:(len(value) + 1)]

count, result = 0, 0

for i in range(0, len(bin_value)):
    if bin_value[i] == '0':
        count = 0
    else:
        count += 1
        result = max(result, count)

print(result)
