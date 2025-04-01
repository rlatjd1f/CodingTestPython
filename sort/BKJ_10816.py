import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().strip().split()))

search_dict = {}
str_list = []
for idx in n_list:
    if idx not in search_dict:
        search_dict[idx] = 1
    else:
        search_dict[idx] += 1

m = int(input())
m_list = list(map(int, input().strip().split()))

for k in m_list:
    if k not in search_dict:
        str_list.append('0')
    else:
        str_list.append(str(search_dict[k]))

print(' '.join(str_list))
