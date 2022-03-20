#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

for i in range(n-1, -1, -1):
    print(arr[i], end=" ")   # end function represents what to be at end of print (usually it is \n newline)


# sample input:
# 4
# 1 4 3 2
