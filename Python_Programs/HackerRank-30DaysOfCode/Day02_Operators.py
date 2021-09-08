#!/bin/python3

# import math   # these were not used to they need to be commented
# import os
# import random
# import re
# import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    tip_cost = tip_percent * meal_cost/100
    tax_cost = tax_percent * meal_cost/100
    total_value = meal_cost + tip_cost + tax_cost
    return round(total_value)


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    print(solve(meal_cost, tip_percent, tax_percent))

# test case:
# 12.00
# 20
# 8
