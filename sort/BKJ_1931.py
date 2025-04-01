import sys

input = sys.stdin.readline

n = int(input())
meet_list = [list(map(int, input().strip().split())) for _ in range(n)]

count = 0
x_start_time, x_end_time = 0, 0

meet_list.sort(key=lambda x: (x[1], x[0]))

for t in meet_list:
    n_start_time = t[0]
    n_end_time = t[1]
    if n_start_time >= x_end_time:
        count += 1
        x_start_time = n_start_time
        x_end_time = n_end_time

print(count)