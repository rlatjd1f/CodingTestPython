import sys

input = sys.stdin.readline

n = int(input())
n_list = [list(map(int, input().strip().split())) for _ in range(n)]

n_list.sort(key=lambda x: (x[0], x[1]))

[print(x[0], x[1]) for x in n_list]