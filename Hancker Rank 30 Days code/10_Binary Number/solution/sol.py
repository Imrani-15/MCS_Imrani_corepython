import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary = bin(n)[2:]
    binary_array = binary.split('0')
    res = max(binary_array)
    print(len(res))