import sys

input = sys.stdin.readline

n = int(input())
infos = []

for i in range(n):
    age, name = map(str, input().strip().split())
    infos.append((int(age), name, i))

infos.sort(key=lambda x: (x[0], x[2]))

for j in infos:
    print(j[0], j[1])
