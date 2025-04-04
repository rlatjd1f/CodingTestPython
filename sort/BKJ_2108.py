import sys

input = sys.stdin.readline

n = int(input())
numbers = []
num_dict = {}

num_cnt_list = []
max_cnt_list = []
maxv = 0

for _ in range(n):
    num = int(input())

    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

    numbers.append(num)
    maxv = max(maxv, num_dict[num])

num_cnt_list = [[key, num_dict[key]] for key in num_dict.keys()]
num_cnt_list.sort(key=lambda x: (x[1], x[0]))
for i in num_cnt_list:
    k, v = i[0], i[1]
    if v == maxv:
        max_cnt_list.append(k)

numbers.sort()
print(int(round(sum(numbers) / len(numbers), 0)))
print(numbers[int(len(numbers) / 2)])

if len(max_cnt_list) > 1:
    print(max_cnt_list[1])
else:
    print(max_cnt_list[0])

print(abs(max(numbers) - min(numbers)))
