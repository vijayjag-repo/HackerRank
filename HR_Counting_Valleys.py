#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sums = 0
    flag = 0
    count = 0
    for i in range(len(s)):
        if(sums<0):
            flag = 1
        if(s[i]=='D'):
            sums-=1
        elif(s[i]=='U'):
            sums+=1
            
        if(sums>=0 and flag==1):
            count+=1
            flag = 0
    return(count)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
