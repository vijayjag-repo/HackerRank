#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    initial_val = len(s)
    count = 0
    ans = 0
    max_limit_n = n//initial_val
    remaining = n%initial_val
    for val in s:
        if(val=='a'):
            count+=1
    ans = count*max_limit_n
    count = 0
    for val in range(0,remaining):
        if(s[val]=='a'):
            count+=1
    return(count+ans)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
