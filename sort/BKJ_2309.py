import sys
from itertools import combinations

input = sys.stdin.readline

h_list = [int(input()) for _ in range(9)]
h_list.sort()

for k in combinations(h_list, 7):
    if sum(k) == 100:
        [print(x) for x in k]
        break
