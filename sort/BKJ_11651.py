import sys

input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().strip().split())) for _ in range(n)]

nums.sort(key=lambda x: (x[1], x[0]))
[print(v[0],v[1]) for v in nums]
