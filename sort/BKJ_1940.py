import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
m_list = list(map(int, input().strip().split()))
m_list.sort()

search_l = 0
search_r = N - 1
res = 0

while search_l < search_r:
    match_num = m_list[search_l] + m_list[search_r]
    if M == match_num:
        res += 1
        search_l += 1
        search_r -= 1
    elif match_num < M:
        search_l += 1
    else:
        search_r -= 1

print(res)
