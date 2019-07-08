#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.

def jumpingOnClouds(c):
    count = 0
    i = 0
    while(i<len(c)-1):
        if(i==len(c)-2):
            return(count+1)
        if(c[i+2]==0):
            i+=2
            count+=1
        elif(c[i+1]==0):
            i+=1
            count+=1
        if(i==len(c)-1): 
            return(count)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
