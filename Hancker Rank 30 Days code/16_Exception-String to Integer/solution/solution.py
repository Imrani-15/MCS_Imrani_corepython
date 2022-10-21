#!/bin/python3

import math
import os
import random
import re
import sys



#if __name__ == "__main__":
S = input().strip()
try:
    interger_value = int(S)
    print(interger_value)
except ValueError:
    print("Bad String")
