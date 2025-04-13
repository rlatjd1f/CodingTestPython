import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
chk_list = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()


def bfs(main_dot):
    res = 0
    queue = deque()
    queue.append(main_dot)
    chk_list[main_dot] = True

    while queue:
        dot = queue.popleft()

        for val in graph[dot]:
            if not chk_list[val]:
                chk_list[val] = True
                queue.append(val)
                res += 1
    return res


print(bfs(1))
