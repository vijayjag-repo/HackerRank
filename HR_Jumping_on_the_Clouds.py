#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    step = 0
    i = 0
    while(i<len(c)):
        if(i==len(c)-3 or i==len(c)-2):
            return(step+1)

        if(c[i+2]==0):
            step+=1
            i = i+2
        elif(c[i+1]==0):
            step+=1
            i = i+1
    return(-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
