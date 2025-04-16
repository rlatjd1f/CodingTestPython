import sys

input = sys.stdin.readline

N = int(input())
s_list = [list(input().strip().split()) for _ in range(N)]

s_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
[print(info[0]) for info in s_list]
