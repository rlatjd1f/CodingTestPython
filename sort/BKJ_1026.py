import sys

input = sys.stdin.readline

n = int(input())

a_list = list(map(int, input().strip().split()))
b_list = list(map(int, input().strip().split()))

a_list.sort()
b_list.sort(reverse=True)

res = 0

for i in range(n):
    res += a_list[i] * b_list[i]

print(res)