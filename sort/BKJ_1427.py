import sys

input = sys.stdin.readline

n = int(input())

n_list = [x for x in list(str(n))]
print(int(''.join(sorted(n_list, reverse=True))))
