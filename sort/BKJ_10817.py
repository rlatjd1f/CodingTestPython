import sys

input = sys.stdin.readline

n = list(map(int, input().strip().split()))

print(sorted(n)[1])
