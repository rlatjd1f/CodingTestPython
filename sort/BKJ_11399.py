import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

rs = 0
sum = 0

for i in sorted(p):
    rs += i
    sum += rs

print(sum)