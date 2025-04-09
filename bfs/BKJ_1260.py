import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(N + 1):
    graph[i].sort()


def dfs(num):
    print(num, end=" ")
    visited_dfs[num] = True
    for val in graph[num]:
        if visited_dfs[val] == False:
            dfs(val)


def bfs(num):
    queue = deque()
    queue.append(num)
    visited_bfs[num] = True
    while queue:
        q = queue.popleft()
        print(q, end=" ")
        for val in graph[q]:
            if visited_bfs[val] == False:
                visited_bfs[val] = True
                queue.append(val)


dfs(V)
print()
bfs(V)
print()
