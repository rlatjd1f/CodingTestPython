import sys

input = sys.stdin.readline

n = int(input())
n_set = set(map(int, input().strip().split()))
res = []

m = int(input())
m_list = list(map(int, input().strip().split()))

for i in m_list:
    if i in n_set:
        res.append(1)
    else:
        res.append(0)

print(' '.join(list(map(str, res))))
