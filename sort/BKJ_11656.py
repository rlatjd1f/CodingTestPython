import sys

input = sys.stdin.readline

S = input().strip()

s_list = [S[i:] for i, w in enumerate(S)]
s_list.sort()

[print(w) for w in s_list]
