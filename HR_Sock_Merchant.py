#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    d = dict()
    for i in range(len(ar)):
        if ar[i] not in d:
            d[ar[i]] = 1
        else:
            d[ar[i]]+=1

    for i in d:
        while(d[i]>=2):
            d[i]-=2
            count+=1
    return(count)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
