import math
import os
import random
import re
import sys
# Complete the 'runningTime' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
def runningTime(arr):
    # Write your code here
    n = len(arr)
    c = 0
    i = 1
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while(arr[j] > temp and j > -1):
            arr[j+1] = arr[j]
            j -= 1
            c += 1
        arr[j+1] = temp
        i += 1
    return c  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = runningTime(arr)
    fptr.write(str(result) + '\n')
    fptr.close()