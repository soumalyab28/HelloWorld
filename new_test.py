#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'selectStock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER saving
#  2. INTEGER_ARRAY currentValue
#  3. INTEGER_ARRAY futureValue
#

def selectStock(saving, currentValue, futureValue):
    # Write your code here
    profit = [0] * len(currentValue)
    
    for i in range(len(currentValue)):
        profit[i] = futureValue[i] - currentValue[i]
    
    md = [[0 for _ in range(len(currentValue))] for _ in range(saving+1)]

    for i in range(1, saving+1):
        for j in range(len(currentValue)):
            if j==0:
                if i>=currentValue[j]:
                    if profit[j] > md[i-1][j]:
                        md[i][j] = profit[j]
                    else:
                        md[i][j] = md[i-1][j]
                else:
                    md[i][j] = 0
            else:
                md[i][j]=md[i][j-1]
                if i > currentValue[j]:
                    if md[i-currentValue[j]][j-1]+profit[j] > md[i][j]:
                        md[i][j] = md[i-currentValue[j]][j-1]+profit[j]
                    if md[i-currentValue[j]][j]>md[i][j]:
                        md[i][j] = md[i-currentValue[j]][j]

return md[saving][len(currentValue)-1]
        

if __name__ == '__main__':