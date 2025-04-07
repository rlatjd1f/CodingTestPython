import sys

input = sys.stdin.readline

n = int(input())
r_list = [int(input()) for _ in range(n)]
r_list.sort()

bf_val = 0
maxv = 0

for i, val in enumerate(r_list):
    cur_val = val

    if cur_val != bf_val:
        maxv = max(maxv, len(r_list[i:]) * cur_val)
    else:
        continue

    bf_val = cur_val

print(maxv)