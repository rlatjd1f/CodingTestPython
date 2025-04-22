import sys

input = sys.stdin.readline

N = int(input())
book_dict = {}

for _ in range(N):
    book_name = input().strip()

    if book_name in book_dict:
        book_dict[book_name] += 1
    else:
        book_dict[book_name] = 1

res_dict = sorted(book_dict.items(), key=lambda x: (-x[1], x[0]))
print(res_dict[0][0])
