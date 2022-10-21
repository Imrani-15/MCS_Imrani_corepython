'''
You are given a string s.
Your task is to
print all possible size k replacement combinations of the string in lexicographic sorted order.
'''
from itertools import combinations_with_replacement
S, k = input().split()
s = sorted(S)
k = int(k)
C= list(combinations_with_replacement(s,k))
for i in C:
    print("".join(i))