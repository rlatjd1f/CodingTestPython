import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().strip().split()))
n_set = sorted(set(n_list))

n_dict = {k: v for v, k in enumerate(n_set)}
res = []

for n in n_list:
    idx = n_dict[n]
    res.append(idx)

print(' '.join(list(map(str, res))))
