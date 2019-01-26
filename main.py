import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = dict()
    for a in ar:
        if a in pairs:
            # print("hi")
            pairs[a] += 1
        else:
            pairs[a] = 1
    total_pairs = 0
    for pair in pairs:
        print(pair)
        if pairs[pair] > 1 and pairs[pair] % 2 == 0:
          pairs[pair] = pairs[pair] / 2
          total_pairs += pairs[pair]

        elif pairs[pair] > 1 and pairs[pair] % 2 == 1:
          pairs[pair] = (pairs[pair]-1) / 2
          total_pairs += pairs[pair]
    return int(total_pairs)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = 9

  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

  result = sockMerchant(n, ar)

  print(result)