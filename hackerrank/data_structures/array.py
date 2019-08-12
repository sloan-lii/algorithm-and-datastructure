#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    result = []
    for i in range(0, len(a)):
        result.append(str(a[len(a)-1-i]))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
