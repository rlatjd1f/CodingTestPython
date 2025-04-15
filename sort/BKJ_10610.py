import sys

input = sys.stdin.readline

N = input().strip()
numbers = list(N)

if '0' not in numbers:
    print(-1)
else:
    if sum(map(int, numbers)) % 3 == 0:
        numbers.sort(reverse=True)
        print(int(''.join(numbers)))
    else:
        print(-1)
