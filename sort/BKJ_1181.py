import sys

input = sys.stdin.readline

n = int(input())
words = list(set([str(input().strip()) for _ in range(n)]))

words.sort()
words.sort(key=lambda x: len(x))

[print(x) for x in words]
