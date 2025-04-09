import sys

imput = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().strip().split()))
num_dict = {v: 1 for v in numbers}

x = int(input())
res_set = set()

for num in numbers:
    diff = x - num
    if diff in num_dict:
        res_set.add((num, diff))

print(len(res_set) // 2) 
