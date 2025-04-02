import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
name_set = set()
name_list = []

for _ in range(n):
    name = input().strip()
    name_set.add(name)

for _ in range(m):
    name = input().strip()
    if name in name_set:
        name_list.append(name)
    else:
        name_set.add(name)

name_list.sort()
print(len(name_list))
[print(x) for x in name_list]
