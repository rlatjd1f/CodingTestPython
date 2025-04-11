import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().strip().split())
graph = [[] for _ in range(n + 1)]
chk_list_dfs = [False for _ in range(n + 1)]
chk_list_bfs = [False for _ in range(n + 1)]

bfs_res, dfs_res = [], []

for _ in range(m):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)

for k in range(len(graph)):
    graph[k].sort()


def dfs(val):
    chk_list_dfs[val] = True
    dfs_res.append(str(val))
    for value in graph[val]:
        if not chk_list_dfs[value]:
            dfs(value)


def bfs(val):
    queue = deque()
    queue.append(val)

    while queue:
        val = queue.popleft()
        chk_list_bfs[val] = True
        bfs_res.append(str(val))
        for value in graph[val]:
            if not chk_list_bfs[value]:
                chk_list_bfs[value] = True
                queue.append(value)


dfs(v)
bfs(v)
print(' '.join(dfs_res))
print(' '.join(bfs_res))
